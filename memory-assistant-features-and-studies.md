# Personal Memory Assistant: Detailed Features & Study Designs

## Table of Contents
1. [System Features](#system-features)
2. [Study Designs](#study-designs)
3. [Technical Architecture](#technical-architecture)
4. [Privacy Framework](#privacy-framework)
5. [Evaluation Metrics](#evaluation-metrics)

---

## System Features

### Core Features (MVP - Year 1)

#### 1. Passive Capture Module

**What it captures:**
- **Conversations:**
  - Video calls (Zoom, Google Meet, Teams)
  - Audio recordings of in-person meetings
  - Phone calls (with permission)
  - Transcribed via Whisper API

- **Documents:**
  - PDFs read or downloaded
  - Web pages visited
  - Notes created (Evernote, OneNote, Apple Notes)
  - Code repositories accessed

- **Screen Activity:**
  - Apps used and when
  - Websites visited
  - Documents open
  - Copy-paste clipboard history (opt-in)

- **Context:**
  - Time and location
  - Calendar events
  - People present (from meeting metadata)
  - Device used

**How it works:**
```python
# Pseudo-code
class CaptureModule:
    def __init__(self):
        self.conversation_recorder = ConversationRecorder()
        self.document_indexer = DocumentIndexer()
        self.screen_monitor = ScreenMonitor()
        self.context_logger = ContextLogger()

    def start_capturing(self):
        # Background processes for each modality
        self.conversation_recorder.start()
        self.document_indexer.start()
        self.screen_monitor.start()
        self.context_logger.start()

    def create_memory_entry(self, data, metadata):
        """
        Create a structured memory entry
        """
        entry = {
            'id': generate_uuid(),
            'timestamp': datetime.now(),
            'data': data,  # text, audio transcript, document content
            'metadata': {
                'source': 'conversation' | 'document' | 'screen' | 'context',
                'privacy_level': 'public' | 'private' | 'sensitive',
                'location': self.context_logger.location,
                'participants': self.context_logger.participants,
                'related_events': []  # links to related memories
            },
            'embedding': embed_with_llm(data)  # vector for semantic search
        }
        return entry
```

#### 2. Multimodal Storage

**Vector Database Schema:**
```
MemoryEntry {
  id: UUID
  timestamp: datetime
  content_type: enum(conversation, document, screen, note)
  text_content: text
  embedding: vector(1536)  // OpenAI ada-002 embedding
  metadata: {
    source_app: string
    location_lat: float
    location_lng: float
    participants: list[string]
    privacy_level: enum(public, private, sensitive)
  }
  related_memories: list[UUID]  // links to related entries
}
```

**Example storage solutions:**
- **Pinecone:** Managed vector DB with semantic search
- **Weaviate:** Open-source, GraphQL interface
- **ChromaDB:** Local-first, privacy-focused
- **pgvector:** PostgreSQL extension (if need SQL + vectors)

#### 3. Retrieval Interface (Conversational)

**Query Examples:**
```
User: "What did I discuss with my supervisor about the deadline?"
System: "On Tuesday, you met with Prof. Hung and discussed:
        - The thesis deadline is April 15th
        - You should submit the draft by March 30th
        - Focus on the experimental results section"

User: "Show me the article on GAM models I read last week"
System: "Here's the arXiv paper 'GAMs for Interpretable ML'
        you read on Feb 5th. [Open PDF]"

User: "What book recommendations have I received?"
System: "You've received these recommendations:
        - 'Thinking, Fast and Slow' from Mai (Jan 15)
        - 'The Design of Everyday Things' from your colleague (Jan 20)"
```

**LLM Pipeline:**
```python
def process_query(user_query, vector_db):
    # 1. Generate search query from natural language
    search_query = llm.extract_search_terms(user_query)
    # 2. Vector search in memory database
    relevant_memories = vector_db.similarity_search(
        query=search_query,
        n_results=10,
        filters=extract_filters(user_query)  # date, person, type
    )
    # 3. Rerank with LLM
    reranked = llm.rerank_memories(user_query, relevant_memories)
    # 4. Generate response
    response = llm.generate_response(
        user_query=user_query,
        memories=reranked[:3],
        explain=True  # show why these results
    )
    return response
```

#### 4. Privacy Dashboard (MVP)

**Features:**
- Visualize captured data over time
- Browse and delete specific memories
- Set privacy levels (public/private/sensitive)
- Disable specific capture sources
- Export all data (GDPR compliance)

**UI Mockup:**
```
┌─────────────────────────────────────────┐
│  Memory Privacy Dashboard                │
├─────────────────────────────────────────┤
│                                          │
│  🔒 Privacy Settings                     │
│  ┌──────────────────────────────────┐  │
│  │ Capture Status: ✅ Active         │  │
│  │                                    │  │
│  │ Conversation Recording: ✅        │  │
│  │ Document Indexing: ✅             │  │
│  │ Screen Monitoring: ✅              │  │
│  │ Location Logging: ✅              │  │
│  └──────────────────────────────────┘  │
│                                          │
│  📊 This Week                           │
│  • 127 conversations recorded           │
│  • 43 documents indexed                 │
│  • 15 queries answered                  │
│                                          │
│  🔍 Browse Memories                     │
│  [Search] [Filter by date/type]          │
│                                          │
│  ┌──────────────────────────────────┐  │
│  │ Feb 10: Meeting with supervisor   │  │
│  │ Privacy: Private    [Delete]      │  │
│  ├──────────────────────────────────┤  │
│  │ Feb 9: Read paper on GAMs         │  │
│  │ Privacy: Public     [Delete]      │  │
│  └──────────────────────────────────┘  │
│                                          │
│  ⚙️ Settings                             │
│  [Export All Data] [Clear All Data]     │
└─────────────────────────────────────────┘
```

---

### Advanced Features (Year 2-3)

#### 5. Explainable Retrieval

**Feature:** Show WHY certain memories are returned

**Example:**
```
User: "What did my supervisor say about the thesis?"
System: "I found 3 relevant memories:

        1. Meeting with Prof. Hung (Feb 10)
           Why: Contains 'supervisor', 'thesis', and was a conversation
           Relevance: 94%

        2. Email from Prof. Hung (Feb 8)
           Why: Contains 'thesis deadline'
           Relevance: 87%

        3. Your notes about thesis (Feb 5)
           Why: About your thesis work
           Relevance: 72%

        Summary: Your supervisor mentioned the deadline is April 15th
        and you should submit the draft by March 30th."
```

**Implementation:**
```python
def explain_retrieval(query, retrieved_memories):
    explanations = []
    for memory in retrieved_memories:
        # Use LLM to explain why this memory is relevant
        explanation = llm.complete(
            f"Query: {query}\n"
            f"Memory: {memory['content']}\n"
            f"Explain why this memory is relevant to the query."
        )
        explanations.append({
            'memory': memory,
            'explanation': explanation,
            'relevance_score': compute_relevance(query, memory)
        })
    return explanations
```

#### 6. Contextual Suggestions

**Feature:** Proactively suggest memories based on current context

**Examples:**
- When opening Zoom: "Last time you met with this person, you discussed X"
- When in location: "You were here 2 weeks ago and noted Y"
- When researching: "You've looked at this topic before: [related memories]"

```python
def suggest_memories(current_context):
    """
    Proactively suggest relevant memories based on context
    """
    context_features = extract_features(current_context)
    suggestions = []

    # Time-based
    if current_context['time'] == 'morning':
        suggestions.extend(get_memories_from('last morning'))

    # Location-based
    if current_context['location'] == 'office':
        suggestions.extend(get_memories_at('office', days_ago=7))

    # Activity-based
    if current_context['app'] == 'zoom':
        meeting_participants = get_meeting_participants()
        suggestions.extend(get_memories_with(participants))

    return rank_suggestions(suggestions, context_features)
```

#### 7. Personalized Summaries

**Feature:** Weekly/monthly summaries of activities

**Example:**
```
Weekly Summary - Feb 3-9, 2026

📚 Research:
• Read 12 papers on Alzheimer's detection
• Made progress on GAM implementation
• Meeting with research group on Thursday

💬 Conversations:
• 27 meetings recorded
• Key topics: thesis progress, Alzheimer's project

📝 Notes Created:
• 8 new notes on research ideas
• 3 to-do items created

🎯 Reminders:
• Thesis draft deadline: March 30 (30 days away)
• Conference abstract due: Feb 20 (11 days away)
```

#### 8. Social Sharing (Optional)

**Feature:** Share memories with others (with permission)

**Use Cases:**
- Share meeting notes with participants
- Collaborative memory for teams
- Family memory sharing

**Privacy:**
- Explicit permission required
- Granular sharing (specific memories, time ranges)
- Revoke access anytime

---

## Study Designs

### Study 1: Formative Study (Diary + Interviews)

**Purpose:** Understand what people want to remember

**Design:**
- **Type:** Diary study + semi-structured interviews
- **Duration:** 2 weeks
- **Participants:** 30 adults (mix of students, professionals)

**Procedure:**
```
Week 1: Diary Study
- Participants receive mobile app
- 3x daily prompts (random times):
  ⚠️ "What did you want to remember in the last 2 hours?"
  📝 Describe the information
  🔒 Privacy sensitivity (1-5 scale)
  💡 How did you try to remember it?

- End-of-day survey:
  📊 How many things did you forget today?
  😤 How frustrating was this?

Week 2: Interviews
- 60-minute semi-structured interviews
- Review diary entries together
- Deep dive into:
  • Most common memory needs
  • Current coping strategies
  • Pain points with existing tools
  • Privacy concerns
  • Ideal memory system
```

**Measures:**
- **Quantitative:**
  - Frequency of memory needs
  - Types of information (categorize: tasks, conversations, facts, etc.)
  - Current tools used
  - Privacy sensitivity levels

- **Qualitative:**
  - Thematic analysis of memory challenges
  - Pain points with current solutions
  - Desired features for ideal system
  - Privacy boundaries

**Expected Findings:**
- Taxonomy of personal memory needs
- Most important information types to capture
- Privacy comfort levels
- Requirements for system design

**Analysis:**
- **Quantitative:** Descriptive statistics, frequency distributions
- **Qualitative:** Thematic analysis (Braun & Clarke)
- **Integration:** Mixed-methods matrix to connect quantitative frequencies with qualitative depth

---

### Study 2: Prototype Evaluation (4-Week Deployment)

**Purpose:** Test initial prototype with real users

**Design:**
- **Type:** Longitudinal field deployment
- **Duration:** 4 weeks
- **Participants:** 20 users (students, knowledge workers)

**Prototype Features (MVP):**
- Conversation recording (meetings)
- Document indexing (PDFs, web pages)
- Basic conversational retrieval
- Privacy dashboard

**Procedure:**
```
Week 0: Onboarding (1 hour)
- Install app and browser extension
- Set privacy preferences
- Tutorial on features
- Baseline survey (current memory strategies)

Weeks 1-4: Deployment
- Use system naturally (daily life)
- Weekly check-ins (15 min):
  • How often did you use it?
  • What worked/didn't work?
  • Privacy concerns?
  • Feature requests

End-of-study: Exit interview (1 hour)
- Overall experience
- What was most useful?
- What was annoying?
- Would you continue using?
- Privacy comfort level
- Suggestions for improvement
```

**Measures:**
- **Usage Analytics:**
  - Number of memories captured per day
  - Number of queries per day
  - Query success rate (found what they wanted)
  - Feature usage patterns

- **User Experience:**
  - System Usability Scale (SUS)
  - NASA-TLX (cognitive load)
  - Privacy Trust Scale
  - Satisfaction ratings

- **Qualitative:**
  - Interview insights
  - Open-ended feedback

**Expected Findings:**
- Which features are most/least used
- User pain points with current design
- Privacy concerns in practice
- UX improvements needed

**Analysis:**
- **Quantitative:** Descriptive stats, correlation analysis (usage patterns vs. satisfaction)
- **Qualitative:** Thematic analysis
- **Mixed:** Triangulate usage logs with interview data

---

### Study 3: Longitudinal Field Study (8 Weeks)

**Purpose:** Understand long-term usage patterns and evolution

**Design:**
- **Type:** Longitudinal field deployment
- **Duration:** 8 weeks
- **Participants:** 50 users

**Enhanced Features:**
- Everything from Study 2, plus:
- Explainable retrieval (show why results returned)
- Contextual suggestions
- Personalized summaries

**Procedure:**
```
Week 0: Onboarding (1 hour)

Weeks 1-8: Deployment
- Natural use
- Biweekly experience sampling:
  ⚡ Get notification 2x/day at random times
  📋 Quick survey (2 min):
    - What are you doing right now?
    - Did you use MemLife today?
    - If yes: What did you look for? Did it help?
    - If no: Why not? (too busy, didn't need it, etc.)
    - Current mood: 😊😐😟
    - Cognitive load: 1-10

- Weekly interviews (30 min) with subset:
  • How is use changing over time?
  • New use cases emerging?
  • Privacy concerns evolving?

Week 8: Exit interview (1 hour)
- Long-term impact assessment
- Comparison with Week 1
- Would you pay for this? ($5-20/month?)
- Future features desired
```

**Measures:**
- **Longitudinal Usage:**
  - Week-by-week usage patterns
  - Adoption trajectory (increasing, decreasing, stable?)
  - Feature adoption over time
  - Query success rate over time

- **Impact Measures:**
  - Memory anxiety scale (pre/post)
  - Productivity self-assessment
  - Cognitive load (NASA-TLX)
  - Life satisfaction

- **Experience Sampling:**
  - Context of use (when, where, doing what)
  - Situational factors affecting use
  - Mood/cognitive load patterns

- **Qualitative:**
  - How relationship with system evolved
  - Trust development over time
  - Integration into daily routines

**Expected Findings:**
- **Adoption Patterns:**
  - Who adopts strongly vs. drops out (and why)
  - Critical period for habit formation (Weeks 2-4?)
  - Features that drive continued use

- **Impact:**
  - Reduced memory anxiety?
  - Improved productivity?
  - Changes in cognitive load

- **Privacy Evolution:**
  - Do privacy concerns decrease over time?
  - What builds trust?

- **Use Cases:**
  - New emergent uses not anticipated
  - Contextual factors influencing use

**Analysis:**
- **Growth Curve Modeling:** Usage trajectories over time
- **Latent Class Analysis:** Identify user types (power users, casual users, dropouts)
- **Experience Sampling Analysis:** Multilevel modeling of within-person variation
- **Qualitative:** Longitudinal thematic analysis

---

### Study 4: Randomized Controlled Trial

**Purpose:** Compare MemLife to existing approaches

**Design:**
- **Type:** Between-subjects RCT
- **Duration:** 6 weeks
- **Participants:** 80 users (20 per condition)

**Conditions:**
1. **MemLife:** Full system with all features
2. **Manual Notes:** Evernote/OneNote (control for manual tools)
3. **General AI:** ChatGPT with memory enabled
4. **Control:** No special tools

**Procedure:**
```
Week 0: Pre-test
- Baseline memory performance test (remember information from reading)
- Memory anxiety scale
- Productivity self-assessment
- Assign to condition

Weeks 1-6: Intervention
- Use assigned tool for 6 weeks
- Complete standardized memory tasks weekly:
  • Read 5 articles
  • Later: Recall what you read
  • Use assigned tool to help

- Weekly surveys:
  • How satisfied with your memory tools?
  • Memory anxiety this week (1-10)
  • Productivity (1-10)

Week 6: Post-test
- Same as pre-test (memory performance, anxiety, productivity)
- Comparison with baseline

Week 6: Exit interview
- Satisfaction with assigned tool
- Perceived benefits/drawbacks
- Would you continue using?
```

**Measures:**
- **Primary Outcome:**
  - Memory recall performance (standardized test)

- **Secondary Outcomes:**
  - Memory anxiety (scale score)
  - Productivity (self-report, task completion)
  - Satisfaction with tools (survey)

- **Mediators:**
  - Frequency of tool use
  - Query success rate
  - Perceived usefulness (TAM scale)

**Expected Findings:**
- MemLife > Manual Notes for memory recall
- MemLife > General AI for personal context
- MemLife > Control for all outcomes
- Mediation: Use frequency → outcomes

**Analysis:**
- **ANCOVA:** Condition effects on post-test (controlling for pre-test)
- **Mediation Analysis:** Does tool use mediate effects?
- **Effect Sizes:** Cohen's d for practical significance
- **Qualitative:** Thematic comparison across conditions

---

## Technical Architecture

### System Components

```
┌─────────────────────────────────────────────────────────┐
│                    User Interface                        │
│  • Web dashboard                                         │
│  • Mobile app (React Native)                            │
│  • Browser extension (Chrome/Firefox)                    │
│  • Conversational interface (voice/text)                 │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│                  Application Layer                        │
│  • Query processing (LLM chain)                          │
│  • Capture orchestration                                 │
│  • Privacy management                                   │
│  • Personalization engine                               │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│                  Data Storage Layer                      │
│  • Vector database (Pinecone/Weaviate)                   │
│  • Document storage (S3/blob storage)                   │
│  • Metadata database (PostgreSQL)                       │
│  • Embedding cache (Redis)                              │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│                 External Services                         │
│  • LLM API (OpenAI/Anthropic)                            │
│  • Speech-to-text (Whisper API)                          │
│  • OCR (Tesseract)                                      │
│  • Calendar API (Google/Outlook)                        │
└─────────────────────────────────────────────────────────┘
```

### Data Flow

**Capture Flow:**
```
User Activity
    ↓
Capture Module (detects activity)
    ↓
Process & Extract (transcribe, extract text)
    ↓
Generate Embedding (LLM API)
    ↓
Store (Vector DB + Metadata DB)
    ↓
Update Privacy Dashboard
```

**Retrieval Flow:**
```
User Query
    ↓
LLM Processing (extract intent, entities)
    ↓
Vector Search (find similar embeddings)
    ↓
Rerank (LLM reranks by relevance)
    ↓
Generate Response (LLM synthesizes answer)
    ↓
Explain Results (show why memories were selected)
    ↓
Present to User
```

### Tech Stack Options

**Frontend:**
- React/Next.js for web dashboard
- React Native for mobile app
- Chrome Extension API for browser extension

**Backend:**
- Python/FastAPI or Node.js/Express
- Async task queue (Celery/Bull) for background processing

**Databases:**
- Vector DB: Pinecone (managed) or Weaviate (self-hosted)
- Metadata: PostgreSQL with pgvector (if want SQL + vectors)
- Cache: Redis for embedding cache, session data

**LLM APIs:**
- OpenAI GPT-4o (best for complex reasoning)
- Anthropic Claude (better for long context)
- Local models (Llama 3, Mistral) for privacy-focused mode

**Other Services:**
- Whisper API for speech-to-text
- Tesseract for OCR (document text extraction)
- Sentry for error tracking
- Datadog for monitoring

---

## Privacy Framework

### Privacy Principles

1. **User Control:**
   - Explicit opt-in for all capture
   - Granular privacy settings (by type, time, content)
   - Easy deletion and export

2. **Transparency:**
   - Always-on privacy dashboard
   - Explain what's captured and why
   - Clear data retention policies

3. **Minimization:**
   - Only capture what's useful
   - Auto-detect and exclude sensitive data
   - Offer privacy-preserving modes

4. **Security:**
   - End-to-end encryption
   - Local processing options
   - Regular security audits

### Privacy Modes

**Full Privacy Mode:**
- Everything processed locally
- No cloud storage
- LLaMA or Mistral models on-device
- Reduced capabilities, maximum privacy

**Balanced Mode (Default):**
- Some local, some cloud
- Sensitive data stays local
- Non-sensitive data in cloud
- Best of both worlds

**Full Feature Mode:**
- Everything in cloud
- Best capabilities (GPT-4o, large vector DB)
- Requires explicit consent
- Recommended for non-sensitive use

### Sensitive Data Detection

**Auto-tagging:**
```python
def detect_sensitive_data(text):
    """
    Auto-detect and tag sensitive content
    """
    sensitive_patterns = {
        'ssn': r'\d{3}-\d{2}-\d{4}',
        'credit_card': r'\d{4}-\d{4}-\d{4}-\d{4}',
        'medical': r'(diagnosis|prescription|doctor)',
        'financial': r'(bank account|salary|income)',
        'passwords': r'(password|pwd)\s*:\s*\S+',
    }

    detected = []
    for label, pattern in sensitive_patterns.items():
        if re.search(pattern, text, re.IGNORECASE):
            detected.append(label)

    return detected

# Auto-redact sensitive content
def redact_sensitive(text, sensitive_labels):
    """
    Redact sensitive content from memories before storage
    """
    for label in sensitive_labels:
        text = re.sub(patterns[label], f'[REDACTED {label}]', text)
    return text
```

---

## Evaluation Metrics

### System Performance Metrics

**Capture Metrics:**
- Capture success rate (% of activities captured)
- Storage efficiency (memory per entry)
- Processing latency (time from capture to indexed)
- Coverage (modalities captured)

**Retrieval Metrics:**
- Query success rate (user finds what they wanted)
- Response latency (time from query to answer)
- Precision/Recall (for evaluation datasets)
- nDCG (ranking quality)

### User Experience Metrics

**Usability:**
- System Usability Scale (SUS)
- NASA-TLX (cognitive load)
- Time to complete tasks
- Error rates

**Satisfaction:**
- User Satisfaction Scale
- NPS (Net Promoter Score)
- Feature satisfaction ratings
- Would you continue using? (yes/no)

**Perceived Impact:**
- Memory Anxiety Scale (custom)
- Productivity self-assessment
- Quality of Life (WHO-QOL BREF)
- Cognitive Load (NASA-TLX)

### Engagement Metrics

**Usage Patterns:**
- Daily/Weekly Active Users
- Average sessions per day
- Average queries per session
- Feature usage breakdown

**Retention:**
- Week-1, Week-4, Week-8 retention
- Churn analysis (who stops using, why)
- Re-engagement patterns

**Adoption:**
- Time to first successful query
- Time to habitual use (3x/week for 3 weeks)
- Feature adoption rate

### Privacy & Trust Metrics

**Privacy Concerns:**
- Privacy Concern Scale (adapted from Buchanan et al.)
- Trust in AI Scale
- Perceived transparency
- Comfort level with capture (per modality)

**Privacy Behaviors:**
- How often users delete memories
- How often users change privacy settings
- Preference for local vs. cloud
- What users choose NOT to capture

---

## Risk Mitigation

### Technical Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| LLM API costs | High | Medium | Use local models for caching, optimize prompts, academic discounts |
| Data storage costs | Medium | Low | Compression, old data archival, prune low-value memories |
| Performance issues | Medium | Medium | Load testing, caching, incremental indexing |
| Privacy breach | Low | High | Encryption, security audits, penetration testing |

### User Study Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Participant attrition | High | Medium | Stipends, engaging design, shorter study periods |
| Low engagement | Medium | High | Onboarding support, regular check-ins, incentives |
| Privacy backlash | Low | High | Strong privacy controls, IRB approval, transparency |
| Technical issues | Medium | Medium | Support channels, fallback options, testing |

---

## Open Questions & Future Directions

### Research Questions for Future Work
- How do memory systems affect long-term memory (do we outsource memory)?
- What are the social implications of AI memory assistants?
- How can we handle contradictory memories (misremembering)?
- Can memory assistants help combat misinformation?

### Technical Directions
- Multimodal memory (images, videos, audio beyond speech)
- Shared/collaborative memories for teams
- Memory compression (summarize old memories)
- Forgetting curves (what to keep vs. prune)

---

This document provides the technical and methodological foundation for the PhD research. Let me know if you want me to expand on any section!
