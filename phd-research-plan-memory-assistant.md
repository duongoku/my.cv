# PhD Research Plan: AI-Powered Personal Memory Assistant for Daily Life

**Candidate:** Nguyen Vu Binh Duong
**Proposed Lab:** Cognitive Interface Lab, NTU Singapore
**Supervisor:** Asst. Prof. Samantha Chan
**Duration:** 3-4 years

---

## Research Title

**"Capturing and Retrieving Everyday Memories: An AI-Powered Multimodal Memory Assistant for Healthy Adults"**

---

## Research Problem

**The Challenge:**

In our information-rich daily lives, we continuously encounter information we want to remember — conversations, documents, photos, ideas, recommendations, tasks. Yet we forget most of it. Existing solutions are inadequate:

- **Note-taking apps** require manual effort and organization
- **Search engines** can't access our personal experiences
- **ChatGPT/memory features** lack personal context, multimodal understanding, and privacy
- **Professional tools** (Microsoft Recall, Rewind.ai) are platform-specific and raise privacy concerns

**The Gap:**

We lack intelligent, privacy-aware systems that can passively capture multimodal information from daily life and provide natural, contextual retrieval when needed — while giving users control over what's stored and how.

---

## Research Vision

**My Goal:** Develop an AI-powered multimodal memory assistant that helps healthy adults capture, organize, and retrieve information from their daily lives through natural conversation — with strong privacy guarantees and explainable AI.

**Key Innovation:**

Instead of requiring manual data entry, the system passively captures information from multiple modalities (conversations, documents, screen activity, locations, photos) and uses large language models to enable natural, contextual retrieval — like having a conversation with your own memory.

---

## Research Questions

### **RQ1: Capture**
What information do people want to remember from their daily lives, and how can we passively capture it across multiple modalities while respecting privacy preferences?

### **RQ2: Representation**
How can we represent multimodal personal experiences in a way that enables efficient, accurate retrieval and explainable AI decisions?

### **RQ3: Retrieval**
How can users naturally query and retrieve information from their personal memory using conversational AI?

### **RQ4: Privacy & Trust**
How can we design memory systems that give users transparency, control, and trust over what's captured and how it's used?

---

## 3-Year Research Plan

### **Year 1: Understanding Needs & Initial Prototype**

**Months 1-3: Literature Review & Problem Definition**
- Systematic review of memory augmentation systems (MemPal, Memoro, Recall, Rewind)
- Analyze limitations of existing approaches
- Define research questions and methodology

**Deliverable:** Literature review paper, research framework

---

**Months 4-6: Formative Study - Memory Needs in Daily Life**
*Study 1: Diary Study & Interviews*

**Research Question:** What do people want to remember from their daily lives, and how do they currently manage it?

**Methods:**
- Diary study: 30 participants log memory needs for 2 weeks
- Semi-structured interviews about current memory strategies
- Analysis of pain points with existing tools

**Sample:** 30 healthy adults (students, professionals, mixed ages)

**Expected Findings:**
- Categories of information people want to remember
- Current coping strategies and their limitations
- Privacy concerns and preferences
- Requirements for ideal memory system

**Deliverable:** CHI paper (or similar HCI venue) on memory needs

---

**Months 7-9: System Design & Initial Prototype**
Based on Study 1 findings, design initial system:

**Core Features:**
- **Passive Capture Module:**
  - Conversation recorder (meetings, calls, in-person)
  - Document/indexer (PDFs, web pages, notes)
  - Activity tracker (apps used, websites visited)
  - Location & context logger

- **Multimodal Storage:**
  - Vector database for semantic embeddings
  - Metadata for temporal, spatial context
  - Privacy tagging system (user-defined sensitivity)

- **Retrieval Interface:**
  - Natural language query (LLM-powered)
  - Conversational refinement
  - Multimodal result presentation

**Tech Stack:**
- LLMs: GPT-4o or Claude for retrieval/generation
- Vector DB: Pinecone or Weaviate
- Speech: Whisper for transcription
- Privacy: Local processing options, encryption

**Deliverable:** Working prototype v1, system design document

---

**Months 10-12: Pilot Evaluation**
*Study 2: Preliminary User Study*

**Research Question:** Can users effectively capture and retrieve information using the prototype?

**Methods:**
- 20 participants use system for 4 weeks
- Weekly check-ins about usage patterns
- Exit interviews about UX, privacy concerns, improvements

**Measures:**
- Capture frequency, retrieval success rate
- Query types, response satisfaction
- Privacy concerns, comfort levels
- Feature usage patterns

**Expected Findings:**
- What works/doesn't in current design
- Privacy comfort levels
- Most common use cases
- UI/UX improvements needed

**Deliverable:** IMWUT or CSCW paper, refined prototype v2

---

### **Year 2: Advanced Features & Field Studies**

**Months 13-15: Enhanced Retrieval & Explainability**
Improve retrieval based on Study 2 findings:

**Add:**
- **Contextual Understanding:** Time, location, recent activity
- **Explainable Retrieval:** Show WHY certain results are returned (like your GAM work!)
- **Personalization:** Learn user preferences over time
- **Proactive Suggestions:** "You asked about X last week, here's related info"

**Research Contribution:** Explainable AI for personal memory retrieval

**Deliverable:** Enhanced prototype v3

---

**Months 16-21: Major Field Study**
*Study 3: Longitudinal Field Deployment*

**Research Question:** How do people use a personal memory assistant in their daily lives over an extended period?

**Methods:**
- 50 participants use system for 8 weeks
- Mixed methods:
  - **Quantitative:** Usage analytics, query logs, success rates
  - **Qualitative:** Biweekly interviews, experience sampling
  - **Longitudinal:** How use patterns evolve over time

**Measures:**
- **Usage Patterns:** When/why people use it
- **Retrieval Accuracy:** Can they find what they need?
- **Impact:** Does it reduce memory anxiety? Improve productivity?
- **Privacy:** Comfort levels over time, concerns
- **Adoption:** What makes people stop/start using it?

**Expected Contributions:**
- Longitudinal understanding of memory assistant adoption
- Design principles for sustainable memory systems
- Privacy framework for personal AI

**Deliverable:** CHI paper (major venue), prototype v4

---

**Months 22-24: Privacy & Trust Focus**
Based on Study 3 privacy concerns, design privacy features:

**Add:**
- **Privacy Dashboard:** Visualize what's captured, enable selective deletion
- **Sensitive Data Detection:** Auto-tag/redact sensitive content
- **Local-Only Mode:** Everything processed locally (privacy-maximized)
- **Sharing Controls:** Granular permissions for shared memories

**Deliverable:** Privacy framework paper (CSCW, USENIX Security)

---

### **Year 3: Advanced Personalization & Final Validation**

**Months 25-27: Adaptive Personalization**
Make system truly personalized:

**Features:**
- **Individual Learning:** Query preferences, result ranking
- **Context Prediction:** Suggest memories based on current situation
- **Memory Summaries:** Weekly/monthly automated summaries
- **Forgotten Reminders:** "You meant to follow up on X..."

**Research Contribution:** Personalization algorithms for memory systems

**Deliverable:** AAAI or AI-HCI venue paper

---

**Months 28-33: Final Randomized Controlled Trial**
*Study 4: Comparative Evaluation*

**Research Question:** How does our system compare to existing approaches (note-taking apps, search, ChatGPT)?

**Methods:**
- 80 participants, 4 conditions (20 each):
  1. Our memory assistant
  2. Manual note-taking (Evernote/OneNote)
  3. General AI (ChatGPT with memory)
  4. Control (no special tools)
- 6-week study with controlled memory tasks + daily use

**Measures:**
- **Objective:** Retrieval accuracy, time to find information, task completion
- **Subjective:** Memory satisfaction, cognitive load, system preference
- **Longitudinal:** Changes over 6 weeks

**Expected Contributions:**
- Empirical validation of memory assistant benefits
- Comparison with existing approaches
- Design guidelines for future systems

**Deliverable:** CHI or IMWUT paper, dissertation

---

**Months 34-36: Analysis, Writing, Defense**
- Compile findings from all studies
- Write dissertation
- Prepare job market materials (if continuing in academia)
- PhD defense

---

## Expected Contributions

### **Theoretical Contributions**
1. Framework for multimodal personal memory capture and retrieval
2. Privacy and trust principles for AI memory systems
3. Longitudinal understanding of memory assistant adoption
4. Explainable AI methods for personal informatics

### **Practical Contributions**
1. Open-source memory assistant system
2. Design guidelines for future memory technologies
3. Privacy toolkit for personal AI applications
4. Best practices for longitudinal deployment studies

### **Societal Impact**
1. Reduce cognitive load and memory anxiety
2. Improve productivity and knowledge management
3. Democratize advanced AI memory tools
4. Advance responsible AI deployment in personal contexts

---

## Publication Plan

| Year | Venue | Topic | Status |
|------|-------|-------|--------|
| 1 | CHI | Memory needs in daily life | Target |
| 1 | IMWUT/CSCW | Prototype evaluation | Target |
| 2 | CHI | Longitudinal field study | Target |
| 2 | CSCW/Security | Privacy & trust | Target |
| 3 | AAAI/AI-HCI | Personalization | Target |
| 3 | CHI/IMWUT | Comparative RCT | Target |

**Goal:** 5-6 top-tier publications, 3-4 first-author

---

## Alignment with Lab

**Cognitive Interface Lab Expertise:**
- ✅ MemPal & Memoro: LLM-based memory assistants (direct extension)
- ✅ HCI methods for user studies and system design
- ✅ Multimodal sensing (wearables, biosignals)
- ✅ Explainable AI (your GAM work + lab's cognitive science focus)
- ✅ Privacy and user autonomy in AI systems

**My Unique Contribution:**
- Combines your ML background (GAM, interpretable AI) with lab's HCI/memory work
- Focus on healthy adults (vs. clinical populations)
- Emphasis on explainability and privacy
- Longitudinal deployment expertise

---

## Feasibility Assessment

### ✅ **Time (3 Years)**
- Multiple short studies (2-8 weeks each)
- No longitudinal clinical validation needed
- System builds incrementally
- Publications can be submitted as studies complete

### ✅ **Resources**
- Software development: Your skills + collaboration
- Participants: Students, professionals (easy recruitment at NTU)
- Computing: Cloud services for LLMs, vector DBs
- IRB: Minimal risk (healthy adults, privacy protections)

### ✅ **Risks & Mitigations**
| Risk | Mitigation |
|------|------------|
| Privacy concerns | Strong privacy framework, user control, IRB approval |
| LLM costs | Local models, API optimization, research credits |
| Participant attrition | Incentives, engaging design, shorter study periods |
| Technical challenges | Incremental development, leverage existing tools |

---

## Beyond the PhD

### **Academic Path**
- Postdoc in HCI/AI (MIT Media Lab, Stanford HCI)
- Faculty position in HCI/CS
- Research scientist at tech labs (Google, Meta, Microsoft Research)

### **Industry Path**
- Product manager for AI/memory features (Google, Microsoft, Apple)
- Founding a startup around personal memory technology
- Research scientist at AI/health tech companies

### **Long-term Vision**
- Enable everyone to have a personalized AI memory companion
- Reduce cognitive load and memory anxiety
- Make human-AI collaboration more natural and beneficial
- Advance responsible, trustworthy AI for personal use

---

## Summary

This PhD will create an AI-powered personal memory assistant that helps healthy adults capture and retrieve information from their daily lives. Through four user studies and iterative system development, I will advance our understanding of how to design multimodal, explainable, and privacy-aware memory systems that genuinely improve people's lives.

The work directly extends the Cognitive Interface Lab's expertise in memory augmentation and LLM-based interfaces, while contributing novel research on multimodal memory representation, explainable retrieval, and privacy in personal AI systems.

**Timeline:** 3 years (flexible to 4)
**Publications:** 5-6 papers (CHI, IMWUT, CSCW, AAAI)
**Impact:** Open-source system, design guidelines, improved daily wellbeing

---

**I'm excited about the potential to help millions of people reduce memory anxiety and cognitive load while advancing the state of the art in human-AI interaction.**
