All use HuggingFace `Trainer` with:
- `problem_type="multi_label_classification"`
- `BCEWithLogitsLoss`
- F1 (micro) evaluation metric

---

## 📊 Dataset Sample

| name | motto | description | topics | url |
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

## 📈 Model Comparison & Results

All models trained on same dataset. RoBERTa-base wins across all metrics.

### Training Results

**RoBERTa-base** ✅ *Selected for inference*

| Epoch | Train Loss | Valid Loss | Accuracy | Precision | Recall | F1 |
|-------|-----------|-----------|----------|-----------|--------|----|
| 0 | 0.0654 | 0.0712 | 0.9703 | 0.369 | 0.263 | 0.266 |
| 3 | 0.0555 | 0.0643 | 0.9753 | 0.487 | 0.365 | 0.369 |
| 6 | 0.0419 | 0.0561 | 0.9813 | 0.595 | 0.448 | 0.463 |
| **9** | **0.0380** | **0.0545** | **0.9828** | **0.591** | **0.468** | **0.484** |

**Micro F1 (final): `0.7683`** 🏆

---

**MiniLM-L12**

| Epoch | Train Loss | Valid Loss | Accuracy | F1 |
|-------|-----------|-----------|----------|----|
| 2 | 0.1140 | 0.1118 | 0.9513 | 0.023 |

**Micro F1: ~0.023** ❌ Failed to converge

---

**DistilBERT**

| Epoch | Train Loss | Valid Loss | Accuracy | F1 |
|-------|-----------|-----------|----------|----|
| 0 | 0.1004 | 0.0977 | 0.9569 | 0.078 |
| 4 | 0.1143 | 0.1118 | 0.9513 | 0.023 |

**Micro F1: ~0.023** ❌ Collapsed after epoch 0

---

### Why RoBERTa-base?

| Metric | RoBERTa-base | MiniLM-L12 | DistilBERT |
|--------|-------------|-----------|-----------|
| Micro F1 | **0.7683** | ~0.023 | ~0.023 |
| Final Accuracy | **98.28%** | 95.13% | 95.13% |
| Convergence | ✅ Steady | ❌ Flat | ❌ Collapsed |
| Epochs trained | 10 | 3 | 5 |

RoBERTa-base steadily improved every epoch — F1 grew from `0.266 → 0.484` (macro) and reached **`0.7683` micro F1**. MiniLM and DistilBERT both collapsed to near-zero F1 after epoch 0, indicating failure to learn label structure.

> **RoBERTa-base selected → converted to ONNX for fast, portable inference.** See `onnx_conversion/`.

---

## 📄 License

MIT — see [LICENSE](LICENSE)

---

<p align="center">Built by <a href="https://github.com/Deb-hridoy">Deb Hridoy</a> · BetaList × HuggingFace × Selenium</p>