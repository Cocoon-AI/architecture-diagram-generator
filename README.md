<p align="center">
  <a href="https://www.atlascloud.ai/?utm_source=github&utm_medium=link&utm_campaign=architecture-diagram-generator">
    <img src="docs/atlas-cloud-logo.png" alt="Atlas Cloud" width="200">
  </a>
</p>

> 🎁 **[Atlas Cloud](https://www.atlascloud.ai/?utm_source=github&utm_medium=link&utm_campaign=architecture-diagram-generator)** is the full-modal AI platform powering architecture diagram generation — Claude Opus 4, GPT-5, DeepSeek-V4 and 56 more frontier LLMs via a unified OpenAI-compatible API. [View all models](https://www.atlascloud.ai/models) · [Coding Plan](https://www.atlascloud.ai/console/coding-plan)

<details>
<summary>📋 59 models available on Atlas Cloud</summary>

| Model | Type |
|-------|------|
| deepseek-ai/deepseek-v4-pro | LLM |
| deepseek-ai/deepseek-v4-0520 | LLM |
| deepseek-ai/deepseek-v4-flash | LLM |
| deepseek-ai/deepseek-r2 | LLM |
| deepseek-ai/deepseek-r2-0528 | LLM |
| deepseek-ai/deepseek-r1-0528 | LLM |
| deepseek-ai/deepseek-r1 | LLM |
| deepseek-ai/deepseek-prover-v2 | LLM |
| moonshot-ai/kimi-k2 | LLM |
| moonshot-ai/kimi-k2-0711 | LLM |
| moonshot-ai/kimi-k1.5-long | LLM |
| qwen/qwen3-235b-a22b | LLM |
| qwen/qwen3-30b-a3b | LLM |
| qwen/qwen3-32b | LLM |
| qwen/qwq-32b | LLM |
| openai/gpt-5 | LLM |
| openai/gpt-5-mini | LLM |
| openai/gpt-4.1 | LLM |
| openai/gpt-4o | LLM |
| openai/o3 | LLM |
| openai/o4-mini | LLM |
| openai/o3-mini | LLM |
| anthropic/claude-sonnet-4-5 | LLM |
| anthropic/claude-opus-4 | LLM |
| anthropic/claude-sonnet-4 | LLM |
| anthropic/claude-haiku-4-5 | LLM |
| google/gemini-2.5-pro | LLM |
| google/gemini-2.5-flash | LLM |
| google/gemini-2.5-flash-lite | LLM |
| google/gemini-2.0-flash | LLM |
| xai/grok-4 | LLM |
| xai/grok-3 | LLM |
| xai/grok-3-mini | LLM |
| meta-llama/llama-4-scout | LLM |
| meta-llama/llama-4-maverick | LLM |
| meta-llama/llama-3.3-70b | LLM |
| cohere/command-a | LLM |
| mistral/mistral-large | LLM |
| minimax/minimax-m1 | LLM |
| 01ai/yi-lightning | LLM |
| seedance/seedance-v1-pro | Video |
| seedance/seedance-v1-pro-fast | Video |
| seedance/seedance-v1-lite | Video |
| kling/kling-v2.1-pro | Video |
| kling/kling-v2.1-standard | Video |
| kling/kling-v1.6-pro | Video |
| kling/kling-v1.6-standard | Video |
| wan2/wan2.1-t2v-turbo | Video |
| wan2/wan2.1-i2v-turbo | Video |
| veo/veo3.1-fast | Video |
| veo/veo3-fast | Video |
| veo/veo3 | Video |
| runway/gen4-turbo | Video |
| stable-diffusion/sd3.5-large | Image |
| flux/flux1.1-pro-ultra | Image |
| flux/flux1.1-pro | Image |
| ideogram/ideogram-v3 | Image |
| recraft/recraft-v3 | Image |
| minimax/hailuo-i2v-01-live | Video |

</details>

---

# Architecture Diagram Generator

**Need an architecture diagram? Get AI to build you one.**

Use [Claude.ai](https://claude.ai) with this special skill to generate professional architecture diagrams in seconds. Describe your system, and Claude creates a beautiful, dark-themed diagram as a standalone HTML file you can open in any browser.

- **No design skills needed** — just describe your architecture in plain English
- **Iterate quickly** — ask Claude to add components, change layouts, or update styles
- **Share easily** — output is a single HTML file, no special software required
- **Export built in** — Copy / PNG / PDF buttons baked into every diagram

![Version](https://img.shields.io/badge/version-1.1-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Claude](https://img.shields.io/badge/Claude-Skill-orange)

## 🚀 Quick Start (3 Steps)

### Step 1: Install the Skill

> ⚠️ Available on Free, Pro, Max, Team, and Enterprise plans (Code Execution must be enabled in **Settings → Capabilities** first)

1. Download [`architecture-diagram.zip`](architecture-diagram.zip)
2. Go to [claude.ai](https://claude.ai) → **Customize** → **Skills**
3. Click the **+** button → **+ Create skill** → **Upload a skill**, then upload the zip file
4. Toggle the skill on

📚 Need help? See the [full installation guide](#-installation) below.

### Step 2: Get Text that Describes Your Architecture

You just need a text description of your system. Pick whichever works for you:

**Option A: Have AI analyze your codebase**

Open your code in Cursor, Claude Code, Windsurf, or ChatGPT and ask:

```
Analyze this codebase and describe the architecture. Include all major
components, how they connect, what technologies they use, and any cloud
services or integrations. Format as a list for an architecture diagram.
```

**Option B: Write it yourself**

Just list your components and how they connect:

```
- React frontend talking to a Node.js API
- PostgreSQL database
- Redis for caching
- Hosted on AWS with CloudFront CDN
```

**Option C: Ask for a typical architecture**

Don't have a specific system? Ask Claude for a starting point:

```
What's a typical architecture for a SaaS application?
```

### Step 3: Generate Your Diagram by Asking Claude to Use the Skill 

Take the output from Step 2 and paste it into [Claude](https://claude.ai) (with the Architecture Diagram Generator skill installed):

```
Use your architecture diagram skill to create an architecture diagram from this description:

[PASTE YOUR ARCHITECTURE DESCRIPTION HERE]
```

That's it! Claude will generate a beautiful HTML file you can open in any browser.

Then!  You can iterate simply by using chat.   Ask Claude:  Please update XYZ to see your diagram update in real time.  You can ask Claude to fix any issues you have with the diagram as well.  

---

### Example Prompts for Common Scenarios

**For a web app:**

```
Create an architecture diagram for a web application with:
- React frontend
- Node.js/Express API
- PostgreSQL database
- Redis cache
- JWT authentication
```

**For AWS serverless:**

```
Create an architecture diagram showing:
- CloudFront CDN
- API Gateway
- Lambda functions (Node.js)
- DynamoDB
- S3 for static assets
- Cognito for auth
```

**For microservices:**

```
Create an architecture diagram for a microservices system with:
- React web app and mobile clients
- Kong API Gateway
- User Service (Go), Order Service (Java), Product Service (Python)
- PostgreSQL, MongoDB, and Elasticsearch databases
- Kafka for event streaming
- Kubernetes orchestration
```

---

## 📸 Examples

### Web Application (React + Node.js + PostgreSQL)

![Web App Architecture](examples/images/web-app.png)

### AWS Serverless (Lambda + API Gateway + DynamoDB)

![AWS Serverless Architecture](examples/images/aws-serverless.png)

### Microservices (Kubernetes + API Gateway)

![Microservices Architecture](examples/images/microservices.png)

## 📤 Export your diagram

Open the HTML file in any modern browser and use the toolbar in the header:

- **📋 Copy** — copy a high-resolution PNG to your clipboard, paste straight into Slides, Docs, or Slack
- **🖼️ PNG** — download a high-resolution PNG file (great for slides and screenshots)
- **📄 PDF** — download a PDF that preserves the dark theme

No install. No command line. Just open the file and click.

## ✨ Features

- **Beautiful dark theme** — Slate-950 background with subtle grid pattern
- **Semantic color coding** — Consistent colors for frontend, backend, database, cloud, and security components
- **Self-contained output** — Single HTML file with embedded CSS and inline SVG
- **Works in any browser** — nothing to install, just open the file
- **Professional typography** — JetBrains Mono for that technical aesthetic
- **Smart layering** — Arrows render cleanly behind component boxes

## 🎨 Color Palette

| Component Type | Color   | Use For                           |
| -------------- | ------- | --------------------------------- |
| Frontend       | Cyan    | Client apps, UI, edge devices     |
| Backend        | Emerald | Servers, APIs, services           |
| Database       | Violet  | Databases, storage, AI/ML         |
| Cloud/AWS      | Amber   | Cloud services, infrastructure    |
| Security       | Rose    | Auth, security groups, encryption |
| External       | Slate   | Generic, external systems         |

## 📦 Installation

> ⚠️ **Available on:** Free, Pro, Max, Team, and Enterprise plans
>
> **Prerequisite:** Code Execution must be enabled before you can upload a custom skill:
> - Free / Pro / Max — turn on under **Settings → Capabilities**
> - Team / Enterprise — admin enables under **Organization settings → Skills**

> 📚 **New to Claude Skills?** Check out the official guide: [Use Skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

### Claude.ai (Recommended)

1. Download [`architecture-diagram.zip`](architecture-diagram.zip)
2. Go to **Customize** → **Skills**
3. Click the **+** button, then **+ Create skill**, then **Upload a skill**
4. Choose the zip file and toggle the skill on

### Claude.ai Projects (Alternative)

1. In your Claude.ai Project, upload the [`architecture-diagram.zip`](architecture-diagram.zip) to the Project Knowledge

### Claude Code CLI

Extract to your skills directory:

```bash
# Global skills
unzip architecture-diagram.zip -d ~/.claude/skills/

# Or project-local
unzip architecture-diagram.zip -d ./.claude/skills/
```

### Manual Setup

Simply ensure both files are accessible to Claude:

```
architecture-diagram/
├── SKILL.md              # Skill instructions
└── resources/
    └── template.html     # Base template
```

## 💾 Output

Claude generates a self-contained HTML file that you can:

- Open directly in any browser
- Share with teammates (just send the file!)
- Include in documentation
- Print or export to PDF
- Host on any static site

## 📐 What's Included in Output

Each generated diagram includes:

1. **Header** — Project title with animated status indicator
2. **Main diagram** — SVG with all components and connections
3. **Summary cards** — 3 info cards highlighting key details
4. **Footer** — Project metadata

## 🛠 Customization

The skill uses a consistent design system, but Claude will adapt:

- **Layout** — Components positioned based on your system's flow
- **Connections** — Arrows showing data flow and relationships
- **Labels** — Protocols, ports, and annotations
- **Groupings** — Security groups, cloud regions, bounded contexts

## 📄 Example Output

The generated HTML structure:

```html
<!DOCTYPE html>
<html>
  <head>
    <!-- Embedded styles, Google Fonts -->
  </head>
  <body>
    <div class="container">
      <div class="header"><!-- Title --></div>
      <div class="diagram-container">
        <svg><!-- Architecture diagram --></svg>
      </div>
      <div class="cards"><!-- Summary cards --></div>
      <p class="footer"><!-- Metadata --></p>
    </div>
  </body>
</html>
```

## 🔧 Technical Details

- **SVG viewBox:** Typically 1000-1100px wide, scales responsively
- **Font:** JetBrains Mono (loaded from Google Fonts)
- **Background:** `#020617` with 40px grid pattern
- **Z-ordering:** Arrows drawn first, masked by opaque backgrounds under transparent component fills

## 📄 Sister skill

For step-by-step workflows that unfold in time — approval flows, runbooks, automation pipelines, [process-flow-diagram-generator](https://github.com/Cocoon-AI/process-flow-diagram-generator) — same design language, different shape language.

## 📝 License

MIT License — Free to use, modify, and distribute.

## 👥 Contributing

Suggestions and improvements welcome! Feel free to:

- Open an issue for bugs or feature requests
- Submit a PR with enhancements
- Share your generated diagrams

## 📬 Contact

**Cocoon AI**
📧 hello@cocoon-ai.com

---

Made with ❤️ by [Cocoon AI](https://cocoon-ai.com)
