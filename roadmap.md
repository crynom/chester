Local AI Companion / AI Lab Roadmap
Vision: Build a modular, local-first AI companion and experimentation platform that teaches the full AI systems stack: inference → tools → memory → retrieval → evaluation → orchestration → agents → specialization.
Phase	Priority	Goal	Deliverables	Key Concepts Learned	Exit Criteria
0	✅ Complete	Local inference foundation	Local model(s), CLI chat app, model loading, chat loop	Local inference, model management	Can have reliable local conversations with multiple models
1	High	Foundation & Architecture	Modular project structure (llm/, voice/, memory/, tools/, agents/, evals/) + config system + session save/load	Software architecture for AI systems	New components can be added without major refactoring
2	High	Voice Interface	STT (Whisper/Faster-Whisper) + TTS (Piper/Kokoro/XTTS)	Speech pipelines, multimodal interaction	Full voice conversation works locally
3	High	Tool Framework	Generic tool-calling system with tool registry and execution layer	Function calling, tool use, agent foundations	Model can invoke tools through a standardized interface
4	High	Web Search	Search tool integrated into tool framework	External knowledge access, retrieval	Model can search current information when needed
5	High	Persistent Memory	SQLite database storing chats, sessions, metadata, facts, preferences	Persistence, memory architecture	Conversations survive restarts and are queryable
6	High	Embeddings & Retrieval	Embedding pipeline + vector search (FAISS/Qdrant/Chroma/LanceDB)	Semantic search, vector databases	Can retrieve related memories from storage
7	High	RAG Layer	Retrieve relevant memories/docs and inject into prompts	Context augmentation, memory recall	Assistant can reference past conversations automatically
8	Medium	Benchmarking Lab	Evaluation harness for models, prompts, memory, retrieval, latency, quality	AI evaluation and experimentation	Can objectively compare configurations
9	Medium	Executive Controller	Central planner that decides tools, retrieval, and task routing	Decision-making systems, orchestration	Requests are planned before execution
10	Medium	Specialized Agents	Planner, Researcher, Coder, Memory Manager (initially same model, different prompts)	Multi-agent systems	Tasks can be delegated to specialist agents
11	Future	Multi-Model Routing	Route tasks to best model (reasoning, coding, planning, etc.)	Model specialization and routing	System chooses optimal model automatically
12	Future	Fine-Tuning Experiments	LoRA/QLoRA training for planner, memory, or coding specialists	Model training, adaptation	At least one custom-trained component exists
13	Future	Knowledge Graph Memory	Structured entity/relation memory alongside vector memory	Symbolic reasoning, graph storage	Long-term memory contains relationships and facts
14	Future	Autonomous Workflows	Goal planning, long-running tasks, self-directed execution loops	Agent autonomy	System can execute multi-step tasks with minimal supervision


## Current Recommended Build Order

0. Local Models + CLI ✅
1. Architecture & Session Persistence
2. Voice (STT + TTS)
3. Tool Framework
4. Web Search
5. SQLite Memory
6. Embeddings + Retrieval
7. RAG
8. Benchmarking Lab
9. Executive Controller
10. Agents
11. Multi-Model Routing
12. Fine-Tuning
13. Knowledge Graphs
14. Autonomous Systems
Copy/Paste Handoff Prompt
Plain Text
I'm building a Local AI Companion / AI Lab.

Current Phase: X

## Roadmap

0. Local inference and CLI (complete)
1. Architecture and session persistence
2. Voice
3. Tool framework
4. Web search
5. SQLite memory
6. Embeddings and retrieval
7. RAG
8. Benchmarking lab
9. Executive controller
10. Specialized agents
11. Multi-model routing
12. Fine-tuning
13. Knowledge graph memory
14. Autonomous workflows
 
Please assume previous phases are complete and help me implement Phase X according to this roadmap while keeping the design modular and future phases in mind.