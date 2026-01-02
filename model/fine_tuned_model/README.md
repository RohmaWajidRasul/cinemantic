---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:396
- loss:MultipleNegativesRankingLoss
base_model: sentence-transformers/all-MiniLM-L6-v2
widget:
- source_sentence: Siblings Lucy, Edmund, Susan and Peter step through a magical wardrobe
    and find the land of Narnia. There, they discover a charming, once peaceful kingdom
    that has been plunged into eternal winter by the evil White Witch, Jadis. Aided
    by the wise and magnificent lion, Aslan, the children lead Narnia into a spectacular,
    climactic battle to be free of the Witch's glacial powers forever.
  sentences:
  - A young street-smart, Nathan Drake and his wisecracking partner Victor “Sully”
    Sullivan embark on a dangerous pursuit of “the greatest treasure never found”
    while also tracking clues that may lead to Nathan’s long-lost brother.
  - After dominating the boxing world, Adonis Creed has been thriving in both his
    career and family life. When a childhood friend and former boxing prodigy, Damien
    Anderson, resurfaces after serving a long sentence in prison, he is eager to prove
    that he deserves his shot in the ring. The face-off between former friends is
    more than just a fight. To settle the score, Adonis must put his future on the
    line to battle Damien — a fighter who has nothing to lose.
  - After his grandfather's death, a man travels with his wife and kids to his hometown,
    where chaos ensues with his relatives over the inheritance.
- source_sentence: The story of 14th century Czech icon and warlord Jan Zizka who
    defeated armies of the Teutonic Order and the Holy Roman Empire.
  sentences:
  - A 17 year old finds out that his girlfriend is dying, so he sets out to give her
    an entire life, in the last year she has left.
  - A young street-smart, Nathan Drake and his wisecracking partner Victor “Sully”
    Sullivan embark on a dangerous pursuit of “the greatest treasure never found”
    while also tracking clues that may lead to Nathan’s long-lost brother.
  - Yeon-du asks her best friend Bora to collect all the information she can about
    Baek Hyun-jin while she is away in the U.S. for heart surgery. Bora decides to
    get close to Baek's best friend, Pung Woon-ho first. However, Bora's clumsy plan
    unfolds in an unexpected direction. In 1999, a year before the new century, Bora,
    who turns seventeen, falls into the fever of first love.
- source_sentence: A young street-smart, Nathan Drake and his wisecracking partner
    Victor “Sully” Sullivan embark on a dangerous pursuit of “the greatest treasure
    never found” while also tracking clues that may lead to Nathan’s long-lost brother.
  sentences:
  - Twenty-five years after a streak of brutal murders shocked the quiet town of Woodsboro,
    a new killer has donned the Ghostface mask and begins targeting a group of teenagers
    to resurrect secrets from the town’s deadly past.
  - A winter night. An isolated house in a small town. Two warring sides must join
    forces to survive an evil tied to one of the field's oldest legends.
  - A 17 year old finds out that his girlfriend is dying, so he sets out to give her
    an entire life, in the last year she has left.
- source_sentence: With the price on his head ever increasing, John Wick uncovers
    a path to defeating The High Table. But before he can earn his freedom, Wick must
    face off against a new enemy with powerful alliances across the globe and forces
    that turn old friends into foes.
  sentences:
  - As viable water is depleted on Earth, a mission is sent to Saturn's moon Titan
    to retrieve sustainable H2O reserves from its alien inhabitants. But just as the
    humans acquire the precious resource, they are attacked by Titan rebels, who don't
    trust that the Earthlings will leave in peace.
  - Darcy and Tom gather their families for the ultimate destination wedding but when
    the entire party is taken hostage, “’Til Death Do Us Part” takes on a whole new
    meaning in this hilarious, adrenaline-fueled adventure as Darcy and Tom must save
    their loved ones—if they don’t kill each other first.
  - A winter night. An isolated house in a small town. Two warring sides must join
    forces to survive an evil tied to one of the field's oldest legends.
- source_sentence: A winter night. An isolated house in a small town. Two warring
    sides must join forces to survive an evil tied to one of the field's oldest legends.
  sentences:
  - After his retirement is interrupted by Gorr the God Butcher, a galactic killer
    who seeks the extinction of the gods, Thor Odinson enlists the help of King Valkyrie,
    Korg, and ex-girlfriend Jane Foster, who now wields Mjolnir as the Mighty Thor.
    Together they embark upon a harrowing cosmic adventure to uncover the mystery
    of the God Butcher’s vengeance and stop him before it’s too late.
  - Shanghai, 1934. In an insect world parallel to that of humans, veteran Inspector
    Sun, a lone spider, leads his last mission against his archenemy the Red Locust,
    before embarking on a well-deserved retirement. His vacation aboard a Pan Am clipper
    between Shanghai and San Francisco comes to an abrupt end when millionaire Dr.
    Spindelthorp is found murdered. What begins as a routine case for Sun will ultimately
    decide the fate of humanity.
  - Decades ago, the USSR developed unkillable sharks and launched them to the moon.
    Today, a team of American astronauts will endure the fight of their lives.
pipeline_tag: sentence-similarity
library_name: sentence-transformers
---

# SentenceTransformer based on sentence-transformers/all-MiniLM-L6-v2

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) <!-- at revision c9745ed1d9f207416be6d2e6f8de32d1f16199bf -->
- **Maximum Sequence Length:** 256 tokens
- **Output Dimensionality:** 384 dimensions
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 256, 'do_lower_case': False, 'architecture': 'BertModel'})
  (1): Pooling({'word_embedding_dimension': 384, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
  (2): Normalize()
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    "A winter night. An isolated house in a small town. Two warring sides must join forces to survive an evil tied to one of the field's oldest legends.",
    'Shanghai, 1934. In an insect world parallel to that of humans, veteran Inspector Sun, a lone spider, leads his last mission against his archenemy the Red Locust, before embarking on a well-deserved retirement. His vacation aboard a Pan Am clipper between Shanghai and San Francisco comes to an abrupt end when millionaire Dr. Spindelthorp is found murdered. What begins as a routine case for Sun will ultimately decide the fate of humanity.',
    'After his retirement is interrupted by Gorr the God Butcher, a galactic killer who seeks the extinction of the gods, Thor Odinson enlists the help of King Valkyrie, Korg, and ex-girlfriend Jane Foster, who now wields Mjolnir as the Mighty Thor. Together they embark upon a harrowing cosmic adventure to uncover the mystery of the God Butcher’s vengeance and stop him before it’s too late.',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.3092, 0.2253],
#         [0.3092, 1.0000, 0.2267],
#         [0.2253, 0.2267, 1.0000]])
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 396 training samples
* Columns: <code>sentence_0</code> and <code>sentence_1</code>
* Approximate statistics based on the first 396 samples:
  |         | sentence_0                                                                          | sentence_1                                                                         |
  |:--------|:------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
  | type    | string                                                                              | string                                                                             |
  | details | <ul><li>min: 18 tokens</li><li>mean: 58.38 tokens</li><li>max: 129 tokens</li></ul> | <ul><li>min: 18 tokens</li><li>mean: 56.2 tokens</li><li>max: 129 tokens</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                                                                                                                                                               | sentence_1                                                                                                                                                                                                                                                                                                                                                                                       |
  |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>Doctor Strange, with the help of mystical allies both old and new, traverses the mind-bending and dangerous alternate realities of the Multiverse to confront a mysterious new adversary.</code>                                                                                                                                                                                   | <code>When the power mysteriously fails, and almost everyone vanishes from a small tourist vessel in the Arctic, fear becomes the master for the three who remain. Forced ashore, the men deteriorate in body and mind until a dark truth emerges that compels them to ally or perish.</code>                                                                                                    |
  | <code>Nearly 5,000 years after he was bestowed with the almighty powers of the Egyptian gods—and imprisoned just as quickly—Black Adam is freed from his earthly tomb, ready to unleash his unique form of justice on the modern world.</code>                                                                                                                                           | <code>The story of 14th century Czech icon and warlord Jan Zizka who defeated armies of the Teutonic Order and the Holy Roman Empire.</code>                                                                                                                                                                                                                                                     |
  | <code>Remy, a seemingly naive and devout young woman, finds herself cast out from her religious cult. With no place to turn, she immerses herself into the underground world of truck stop sex workers. Under the watchful eye of their matriarch and an enigmatic local lawman, Remy navigates between her strained belief system and the code to find her true calling in life.</code> | <code>Peter is searching for his long-lost sister when he crosses paths with a fortune teller in the market square. His one one question is: is his sister still alive? The answer, that he must find a mysterious elephant and the magician who will conjure it, sets Peter off on a journey to complete three seemingly impossible tasks that will change the face of his town forever.</code> |
* Loss: [<code>MultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim",
      "gather_across_devices": false
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 128
- `per_device_eval_batch_size`: 128
- `num_train_epochs`: 2
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: no
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 128
- `per_device_eval_batch_size`: 128
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1
- `num_train_epochs`: 2
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.0
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `save_safetensors`: True
- `save_on_each_node`: False
- `save_only_model`: False
- `restore_callback_states_from_checkpoint`: False
- `no_cuda`: False
- `use_cpu`: False
- `use_mps_device`: False
- `seed`: 42
- `data_seed`: None
- `jit_mode_eval`: False
- `bf16`: False
- `fp16`: False
- `fp16_opt_level`: O1
- `half_precision_backend`: auto
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `local_rank`: 0
- `ddp_backend`: None
- `tpu_num_cores`: None
- `tpu_metrics_debug`: False
- `debug`: []
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_prefetch_factor`: None
- `past_index`: -1
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `adafactor`: False
- `group_by_length`: False
- `length_column_name`: length
- `project`: huggingface
- `trackio_space_id`: trackio
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `skip_memory_metrics`: True
- `use_legacy_prediction_loop`: False
- `push_to_hub`: False
- `resume_from_checkpoint`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_private_repo`: None
- `hub_always_push`: False
- `hub_revision`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_inputs_for_metrics`: False
- `include_for_metrics`: []
- `eval_do_concat_batches`: True
- `fp16_backend`: auto
- `push_to_hub_model_id`: None
- `push_to_hub_organization`: None
- `mp_parameters`: 
- `auto_find_batch_size`: False
- `full_determinism`: False
- `torchdynamo`: None
- `ray_scope`: last
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: no
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: True
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Framework Versions
- Python: 3.14.1
- Sentence Transformers: 5.1.2
- Transformers: 4.57.3
- PyTorch: 2.9.1+cpu
- Accelerate: 1.12.0
- Datasets: 4.4.1
- Tokenizers: 0.22.1

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

#### MultipleNegativesRankingLoss
```bibtex
@misc{henderson2017efficient,
    title={Efficient Natural Language Response Suggestion for Smart Reply},
    author={Matthew Henderson and Rami Al-Rfou and Brian Strope and Yun-hsuan Sung and Laszlo Lukacs and Ruiqi Guo and Sanjiv Kumar and Balint Miklos and Ray Kurzweil},
    year={2017},
    eprint={1705.00652},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->