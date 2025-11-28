---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:25000
- loss:MultipleNegativesRankingLoss
base_model: sentence-transformers/all-MiniLM-L6-v2
widget:
- source_sentence: Shaggy is turned into a werewolf, and it's up to Scooby, Scrappy
    and Shaggy's girlfriend to help him win a race against other monsters, and become
    human again.
  sentences:
  - While farm-sitting, George accidentally lets the farm animals escape. Ted, George
    and wannabe cowboy Emmett must round 'em up, accounting for every animal -- and
    emerging with some new skills, to boot.
  - A documentation of and meditation on the internal and external worlds of gender
    dysphoria, as experienced by, shot by, narrated by, and written out by the subject
    at the film’s core. Audio description and open captions are implemented throughout
    the film to create a conversation between the typically inaudible and ineligible
    voices of the queer body and mind.
  - Brimming with action while incisively examining the nature of truth, "Rashomon"
    is perhaps the finest film ever to investigate the philosophy of justice. Through
    an ingenious use of camera and flashbacks, Kurosawa reveals the complexities of
    human nature as four people recount different versions of the story of a man's
    murder and the rape of his wife.
- source_sentence: The evil Dr. Kochin uses the dragon balls to resurrect his mentor,
    Dr. Wheelo, in an effort to take over the world. Dr. Wheelo, his body having been
    destroyed by the avalanche that killed him fifty years before, desires the body
    of the strongest fighter in the world as his new vessel. Believing Roshi to be
    the world's strongest warrior, Dr. Kochin abducts Bulma and forces Roshi to surrender
    himself to save her. When Goku hears of their abduction, he goes to their rescue.
  sentences:
  - In the town of Saima, when summer is about to begin, a group of six high school
    students intend to live a secret adventure by spending seven carefree days in
    a ruined mining facility.
  - Mike Milo, a one-time rodeo star and washed-up horse breeder, takes a job from
    an ex-boss to bring the man's young son home from Mexico.
  - A quest that begins as a personal vendetta for the fierce Cimmerian warrior soon
    turns into an epic battle against hulking rivals, horrific monsters, and impossible
    odds, as Conan realizes he is the only hope of saving the great nations of Hyboria
    from an encroaching reign of supernatural evil.
- source_sentence: Tony, a promising young motorcycle racer, is forced to do perilous
    drug runs to save the mother of his child from a dangerous mobster.
  sentences:
  - At the start of World War I, Paul Baumer is a young German patriot, eager to fight.
    Indoctrinated with propaganda at school, he and his friends eagerly sign up for
    the army soon after graduation. But when the horrors of war soon become too much
    to bear, and as his friends die or become gravely wounded, Paul questions the
    sanity of fighting over a few hundreds yards of war-torn countryside.
  - 'Rick and Evelyn O’Connell, along with their 8-year-old son Alex, discover the
    key to the legendary Scorpion King’s might: the fabled Bracelet of Anubis. Unfortunately,
    a newly resurrected Imhotep has designs on the bracelet as well, and isn’t above
    kidnapping its new bearer, Alex, to gain control of Anubis’s otherworldly army.'
  - When their trip to San Lorenzo takes a turn for the worst, Arnold and his classmate’s
    only hope of getting home is retracing the dangerous path that led to Arnold's
    parents' disappearance.
- source_sentence: ¡Que viva México! was a film project undertaken in 1931-32 by Soviet
    film-maker Sergei Eisenstein for American socialist author Upton Sinclair and
    several investors, which Eisenstein eventually conceived as an episodic portrayal
    of Mexican culture and politics from pre-Conquest civilization to the Mexican
    revolution. Over 200,000 feet of silent film were shot before production had to
    be stopped due to exhaustion of finances and Stalin's demands that Eisenstein
    return to the USSR.  This is one of several attempts to make a feature film out
    of the existing footage, here according to Eisenstein's skeletal outline and under
    the supervision of Gregori Alexandrov, Eisenstein's long-time collaborator, including
    on this project.
  sentences:
  - 'Records the battle for the survival of the big cats and reveals intimate details
    of their lives. The animals they prey on are also in the film: tigers couldn’t
    survive without sika deer, Altai wapiti, wild boars and Asian black bears. Guiding
    the viewer through the film, an elder tiger tells the story of his cub, born in
    a conservation area, the year after he leaves his mother.'
  - Disney's irresistible talking puppies are back in an all-new movie that takes
    them far across town to a mysterious mansion where something very spooky is going
    on.
  - Murphy is an American living in Paris who enters a highly sexually and emotionally
    charged relationship with the unstable Electra. Unaware of the seismic effect
    it will have on their relationship, they invite their pretty neighbor into their
    bed.
- source_sentence: Washed-up MMA fighter Cole Young, unaware of his heritage, and
    hunted by Emperor Shang Tsung's best warrior, Sub-Zero, seeks out and trains with
    Earth's greatest champions as he prepares to stand against the enemies of Outworld
    in a high stakes battle for the universe.
  sentences:
  - A strange old woman allows a teenage runaway and a young orphan to stay in an
    abandoned house that overlooks the sea. However, when a menacing entity threatens
    their new home, they must band together and face their fears to save it.
  - 'Having cleared his name, genius mechanic Lino has only one goal in mind: getting
    revenge on the corrupt cops who killed his brother and his mentor.'
  - A Bollywood update of Jane Austen's classic tale, in which Mrs. Bakshi is eager
    to find suitable husbands for her four unmarried daughters. When the rich single
    gentlemen Balraj and Darcy come to visit, the Bakshis have high hopes, though
    circumstance and boorish opinions threaten to get in the way of romance.
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
    "Washed-up MMA fighter Cole Young, unaware of his heritage, and hunted by Emperor Shang Tsung's best warrior, Sub-Zero, seeks out and trains with Earth's greatest champions as he prepares to stand against the enemies of Outworld in a high stakes battle for the universe.",
    'Having cleared his name, genius mechanic Lino has only one goal in mind: getting revenge on the corrupt cops who killed his brother and his mentor.',
    "A Bollywood update of Jane Austen's classic tale, in which Mrs. Bakshi is eager to find suitable husbands for her four unmarried daughters. When the rich single gentlemen Balraj and Darcy come to visit, the Bakshis have high hopes, though circumstance and boorish opinions threaten to get in the way of romance.",
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.8178, 0.7002],
#         [0.8178, 1.0000, 0.6888],
#         [0.7002, 0.6888, 1.0000]])
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

* Size: 25,000 training samples
* Columns: <code>sentence_0</code> and <code>sentence_1</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence_0                                                                          | sentence_1                                                                         |
  |:--------|:------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
  | type    | string                                                                              | string                                                                             |
  | details | <ul><li>min: 11 tokens</li><li>mean: 61.23 tokens</li><li>max: 234 tokens</li></ul> | <ul><li>min: 13 tokens</li><li>mean: 62.6 tokens</li><li>max: 251 tokens</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                                                                                  | sentence_1                                                                                                                                                                                                                |
  |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>As a young and naive recruit in Vietnam, Chris Taylor faces a moral crisis when confronted with the horrors of war and the duality of man.</code>                                                                                                                                                     | <code>A widow with three children hires a handyman to fix her house during a major storm. When not doing home repairs, he shares his philosophy of believing in the power of the universe to deliver what we want.</code> |
  | <code>A fictional history of two legendary revolutionaries' journey away from home before they began fighting for their country in the 1920s.</code>                                                                                                                                                        | <code>A 16-year-old girl visits her gay half-brother and ends up seducing his boyfriend, thus wreaking havoc on all of their lives.</code>                                                                                |
  | <code>Anton is a cheerful but exceedingly non-ambitious 17-year-old stoner who lives to stay buzzed, watch TV, and moon over Molly, the beautiful girl who lives next door. However, it turns out that the old cliché about idle hands being the devil's playground has a kernel of truth after all.</code> | <code>After Homer accidentally pollutes the town's water supply, Springfield is encased in a gigantic dome by the EPA and the Simpsons are declared fugitives.</code>                                                     |
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

- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 32
- `num_train_epochs`: 4
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: no
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 32
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
- `num_train_epochs`: 4
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

### Training Logs
| Epoch  | Step | Training Loss |
|:------:|:----:|:-------------:|
| 0.6394 | 500  | 3.4969        |
| 1.2788 | 1000 | 3.0242        |
| 1.9182 | 1500 | 2.9052        |
| 2.5575 | 2000 | 2.7764        |
| 3.1969 | 2500 | 2.736         |
| 3.8363 | 3000 | 2.6828        |


### Framework Versions
- Python: 3.13.2
- Sentence Transformers: 5.1.2
- Transformers: 4.57.3
- PyTorch: 2.9.1
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