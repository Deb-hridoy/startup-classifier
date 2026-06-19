All use HuggingFace `Trainer` with:
- `problem_type="multi_label_classification"`
- `BCEWithLogitsLoss`
- F1 (micro) evaluation metric

---

## 📊 Dataset Sample

| name | motto | description | genres | url |
|------|-------|-------------|--------|-----|
| OutboundGateway | Route traffic securely... | Provides HTTPS... | Internet Service Providers, Security | betalist.com/... |
| Flux Plugins | Speed up WordPress... | AI-powered image, SEO... | Blogging, Optimization | betalist.com/... |

**Shape:** `(21408, 5)` · **Nulls:** `0`

---

## 🧠 Models

| Model | Type | Notes |
|-------|------|-------|
| DistilBERT | Encoder | Fast baseline |
| RoBERTa-base | Encoder | Best performance |
| MiniLM-L12 | Encoder | Efficient deployment |

All exported to ONNX for inference — see `onnx_conversion/`.

---

## 📄 License

MIT — see [LICENSE](LICENSE)

---

<p align="center">Built by <a href="https://github.com/Deb-hridoy">Deb Hridoy</a> · BetaList × HuggingFace × Selenium</p>