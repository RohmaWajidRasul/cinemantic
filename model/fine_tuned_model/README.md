---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:276
- loss:MultipleNegativesRankingLoss
base_model: sentence-transformers/all-MiniLM-L6-v2
widget:
- source_sentence: Sayen is hunting down the men who murdered her grandmother. Using
    her training and knowledge of nature, she is able to turn the tables on them,
    learning of a conspiracy from a corporation that threatens her people's ancestral
    lands.
  sentences:
  - Reporters Loretta McLaughlin and Jean Cole bravely pursue the story of the Boston
    Strangler at great personal risk, putting their own lives on the line in their
    quest to uncover the truth.
  - Set more than a decade after the events of the first film, learn the story of
    the Sully family (Jake, Neytiri, and their kids), the trouble that follows them,
    the lengths they go to keep each other safe, the battles they fight to stay alive,
    and the tragedies they endure.
  - A journey deep into an uncharted and treacherous land, where fantastical creatures
    await the legendary Clades—a family of explorers whose differences threaten to
    topple their latest, and by far most crucial, mission.
- source_sentence: Liliana is the dream girl of many of her co-workers, among them
    "Piquiña", an ugly and ordinary charlatan who, convinced of his irresistible attractiveness,
    launches into her conquest during the celebration of the company's "novena". Liliana,
    who can't stand "Piquíña", makes it clear to him that the only way she would be
    with him would be if he were the last man on earth.
  sentences:
  - An American priest working in Mexico is considered a saint by many local parishioners.
    However, due to a botched exorcism, he carries a secret that’s eating him alive
    until he gets an opportunity to face his demon one final time.
  - All Gary wants is to make awesome home movies with his best buds. All his older
    sister Samantha wants is to hang with the cool kids. When their parents head out
    of town one Halloween weekend, an all-time rager of a teen house party turns to
    terror when aliens attack, forcing the siblings to band together to survive the
    night.
  - 'Blindsided by a new generation of blazing-fast racers, the legendary Lightning
    McQueen is suddenly pushed out of the sport he loves. To get back in the game,
    he will need the help of an eager young race technician with her own plan to win,
    inspiration from the late Fabulous Hudson Hornet, and a few unexpected turns.
    Proving that #95 isn''t through yet will test the heart of a champion on Piston
    Cup Racing’s biggest stage!'
- source_sentence: After witnessing a grotesque murder at a party in her new town,
    a teenager starts having strange visions and bizarre desires.
  sentences:
  - Mario and Luigi, plumbers from Brooklyn, find themselves in an alternate universe
    where evolved dinosaurs live in hi-tech squalor. They're the only hope to save
    our universe from invasion by the dino dictator, Koopa.
  - Royal Air Force pilot Lt. Kate Sinclair is on her final flight mission when her
    jet is shot down over one of the most dangerous rebel strongholds in Afghanistan.
    She finds refuge in an abandoned underground bunker where deadly man-made creatures
    known as Ravagers — half-human, half-alien, and hungry for human flesh — are awakened.
  - The Red Ribbon Army, an evil organization that was once destroyed by Goku in the
    past, has been reformed by a group of people who have created new and mightier
    Androids, Gamma 1 and Gamma 2, and seek vengeance against Goku and his family.
- source_sentence: Mario and Luigi, plumbers from Brooklyn, find themselves in an
    alternate universe where evolved dinosaurs live in hi-tech squalor. They're the
    only hope to save our universe from invasion by the dino dictator, Koopa.
  sentences:
  - When the power mysteriously fails, and almost everyone vanishes from a small tourist
    vessel in the Arctic, fear becomes the master for the three who remain. Forced
    ashore, the men deteriorate in body and mind until a dark truth emerges that compels
    them to ally or perish.
  - Thirteen-year-old Mei is experiencing the awkwardness of being a teenager with
    a twist – when she gets too excited, she transforms into a giant red panda.
  - A stubborn and hotheaded minor league basketball coach is forced to train a Special
    Olympics team when he is sentenced to community service.
- source_sentence: The hottest biotech company in the world has discovered they can
    clone history’s most influential people from the dead. Now, they are auctioning
    clones of Michelangelo, Galileo, Vivaldi, and others for tens of millions of dollars
    to the world’s ultra-rich. But when they steal the Shroud of Turin and clone the
    DNA of Jesus Christ, all hell breaks loose.
  sentences:
  - When five lovely young girls who hate studying hire part-time tutor Futaro, he
    guides not only their education but also their hearts. Time spent has brought
    them all closer, with feelings growing within the girls and Futaro. As they finish
    their third year of high school and their last school festival approaches, they
    set their sights on what’s next. Is there a future with one of them and Futaro?
  - Detective James Knight 's last-minute assignment to the Independence Day shift
    turns into a race to stop an unbalanced ambulance EMT from imperiling the city's
    festivities. The misguided vigilante, playing cop with a stolen gun and uniform,
    has a bank vault full of reasons to put on his own fireworks show... one that
    will strike dangerously close to Knight's home.
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
    'The hottest biotech company in the world has discovered they can clone history’s most influential people from the dead. Now, they are auctioning clones of Michelangelo, Galileo, Vivaldi, and others for tens of millions of dollars to the world’s ultra-rich. But when they steal the Shroud of Turin and clone the DNA of Jesus Christ, all hell breaks loose.',
    'Decades ago, the USSR developed unkillable sharks and launched them to the moon. Today, a team of American astronauts will endure the fight of their lives.',
    'When five lovely young girls who hate studying hire part-time tutor Futaro, he guides not only their education but also their hearts. Time spent has brought them all closer, with feelings growing within the girls and Futaro. As they finish their third year of high school and their last school festival approaches, they set their sights on what’s next. Is there a future with one of them and Futaro?',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.1682, 0.1853],
#         [0.1682, 1.0000, 0.0770],
#         [0.1853, 0.0770, 1.0000]])
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

* Size: 276 training samples
* Columns: <code>sentence_0</code> and <code>sentence_1</code>
* Approximate statistics based on the first 276 samples:
  |         | sentence_0                                                                          | sentence_1                                                                          |
  |:--------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
  | type    | string                                                                              | string                                                                              |
  | details | <ul><li>min: 18 tokens</li><li>mean: 58.72 tokens</li><li>max: 129 tokens</li></ul> | <ul><li>min: 18 tokens</li><li>mean: 59.11 tokens</li><li>max: 111 tokens</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                                                                                                                                                                                                                                 | sentence_1                                                                                                                                                                                                                                                                      |
  |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>Rich and powerful Simon Qing has been schooled in the ways of sex by his virile father, but is still a virgin. That is, until he meets his first love Violetta who has fun with him all over his father’s estate. Their love does not last, so Simon embarks on a journey. Along the way he meets the comely nun Moon whom Simon deflowers and then marries. He then becomes enamored of Golden Lotus but she is married to dwarf Wu Da-Lang.</code> | <code>Between personal obligations and training for his next big fight against an opponent with ties to his family's past, Adonis Creed is up against the challenge of his life.</code>                                                                                         |
  | <code>When the power mysteriously fails, and almost everyone vanishes from a small tourist vessel in the Arctic, fear becomes the master for the three who remain. Forced ashore, the men deteriorate in body and mind until a dark truth emerges that compels them to ally or perish.</code>                                                                                                                                                              | <code>With the price on his head ever increasing, John Wick uncovers a path to defeating The High Table. But before he can earn his freedom, Wick must face off against a new enemy with powerful alliances across the globe and forces that turn old friends into foes.</code> |
  | <code>This Christmas, Homer surprises Marge with the ultimate gift: an unforgettable performance from Italian opera superstar Andrea Bocelli and his children Matteo and Virginia.</code>                                                                                                                                                                                                                                                                  | <code>The Elric brothers’ long and winding journey comes to a close in this epic finale, where they must face off against an unworldly, nationwide threat.</code>                                                                                                               |
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
- Python: 3.12.6
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