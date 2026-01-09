---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:137
- loss:MultipleNegativesRankingLoss
base_model: sentence-transformers/all-MiniLM-L6-v2
widget:
- source_sentence: It has been a year since Mic Mic and Oscar returned from their
    incredible adventure. And now, after a diabolical plan by Vulture to sabotage
    the delivery of the Grizzly cub to his opponent in the American presidential elections,
    Mic Mic, Oscar, Panda teenager and Stork set off on another great adventure as
    they ride a zeppelin to return little Grizzly to its rightful parents and save
    the American elections and the whole continent from an erupting volcano.
  sentences:
  - A brilliant toy company roboticist uses artificial intelligence to develop M3GAN,
    a life-like doll programmed to emotionally bond with her newly orphaned niece.
    But when the doll's programming works too well, she becomes overprotective of
    her new friend with terrifying results.
  - A boy is given the ability to become an adult superhero in times of need with
    a single magic word.
  - 'When a team of mercenaries breaks into a wealthy family compound on Christmas
    Eve, taking everyone inside hostage, the team isn’t prepared for a surprise combatant:
    Santa Claus is on the grounds, and he’s about to show why this Nick is no saint.'
- source_sentence: An extraordinary young girl discovers her superpower and summons
    the remarkable courage, against all odds, to help others change their stories,
    whilst also taking charge of her own destiny. Standing up for what's right, she's
    met with miraculous results.
  sentences:
  - 'When a team of mercenaries breaks into a wealthy family compound on Christmas
    Eve, taking everyone inside hostage, the team isn’t prepared for a surprise combatant:
    Santa Claus is on the grounds, and he’s about to show why this Nick is no saint.'
  - With the price on his head ever increasing, John Wick uncovers a path to defeating
    The High Table. But before he can earn his freedom, Wick must face off against
    a new enemy with powerful alliances across the globe and forces that turn old
    friends into foes.
  - Deep inside the mountain of Dovre, something gigantic awakens after being trapped
    for a thousand years. Destroying everything in its path, the creature is fast
    approaching the capital of Norway. But how do you stop something you thought only
    existed in Norwegian folklore?
- source_sentence: After a catastrophic crash on an unknown planet, pilot Mills quickly
    discovers he's actually stranded on Earth…65 million years ago. Now, with only
    one chance at rescue, Mills and the only other survivor, Koa, must make their
    way across an unknown terrain riddled with dangerous prehistoric creatures in
    an epic fight to survive.
  sentences:
  - While vacationing at a remote cabin, a young girl and her two fathers are taken
    hostage by four armed strangers who demand that the family make an unthinkable
    choice to avert the apocalypse. With limited access to the outside world, the
    family must decide what they believe before all is lost.
  - After a heroic job of successfully landing his storm-damaged aircraft in a war
    zone, a fearless pilot finds himself between the agendas of multiple militias
    planning to take the plane and its passengers hostage.
  - A semi-retired special ops assassin and a DEA agent cross paths on separate missions
    to stop a cyber terrorist organization that has built a dangerous machine threatening
    to attack the power grid and bring catastrophe to the world.
- source_sentence: While working underground to fix a water main, Brooklyn plumbers—and
    brothers—Mario and Luigi are transported down a mysterious pipe and wander into
    a magical new world. But when the brothers are separated, Mario embarks on an
    epic quest to find Luigi.
  sentences:
  - Paul Baumer and his friends Albert and Muller, egged on by romantic dreams of
    heroism, voluntarily enlist in the German army. Full of excitement and patriotic
    fervour, the boys enthusiastically march into a war they believe in. But once
    on the Western Front, they discover the soul-destroying horror of World War I.
  - When a plane crashes at sea, dolphins rescue a little boy and raise him as family.
    He lives a carefree life beneath the waves until an evil monster seizes power
    over the underwater world. The boy is banished to dry land, where a kind-hearted
    captain takes him in. With the captain’s help, the boy sets out on a journey to
    solve the mystery of his true identity.
  - An extraordinary young girl discovers her superpower and summons the remarkable
    courage, against all odds, to help others change their stories, whilst also taking
    charge of her own destiny. Standing up for what's right, she's met with miraculous
    results.
- source_sentence: Ophelia, a young nun recently arriving in the town of San Ramon,
    is forced to perform an exorcism on a pregnant woman in danger of dying. Just
    when she thinks her possession has ended, she discovers that the evil presence
    hasn't disappeared yet. The director of the award-winning Here Comes the Devil
    and Late Phases adds a new twist to possession movies in one of this year's Latin
    American horror surprises.
  sentences:
  - Erstwhile Special Forces operative Doc Alexander is asked to broker a truce with
    the Mexican drug cartel in secrecy. When Oklahoma Governor Richard Jeffs celebrates
    the execution of a high-ranking cartel member on TV, his Chief of Staff and Doc
    inform him about the peace he just ended. But it’s too late, as Cuco, the cartel’s
    hatchet man, has set his vengeful sights on Doc’s daughter Dixie.
  - Following a mysterious disappearance on a jump, a group of skydivers experiences
    paranormal occurrences that leave them fighting for their lives.
  - Valeria's joy at becoming a first-time mother is quickly taken away when she's
    cursed by a sinister entity. As danger closes in, she's forced deeper into a chilling
    world of dark magic that threatens to consume her.
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
    "Ophelia, a young nun recently arriving in the town of San Ramon, is forced to perform an exorcism on a pregnant woman in danger of dying. Just when she thinks her possession has ended, she discovers that the evil presence hasn't disappeared yet. The director of the award-winning Here Comes the Devil and Late Phases adds a new twist to possession movies in one of this year's Latin American horror surprises.",
    'Following a mysterious disappearance on a jump, a group of skydivers experiences paranormal occurrences that leave them fighting for their lives.',
    'Erstwhile Special Forces operative Doc Alexander is asked to broker a truce with the Mexican drug cartel in secrecy. When Oklahoma Governor Richard Jeffs celebrates the execution of a high-ranking cartel member on TV, his Chief of Staff and Doc inform him about the peace he just ended. But it’s too late, as Cuco, the cartel’s hatchet man, has set his vengeful sights on Doc’s daughter Dixie.',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.2794, 0.1137],
#         [0.2794, 1.0000, 0.0137],
#         [0.1137, 0.0137, 1.0000]])
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

* Size: 137 training samples
* Columns: <code>sentence_0</code> and <code>sentence_1</code>
* Approximate statistics based on the first 137 samples:
  |         | sentence_0                                                                          | sentence_1                                                                          |
  |:--------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
  | type    | string                                                                              | string                                                                              |
  | details | <ul><li>min: 22 tokens</li><li>mean: 58.57 tokens</li><li>max: 129 tokens</li></ul> | <ul><li>min: 22 tokens</li><li>mean: 55.96 tokens</li><li>max: 106 tokens</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                                                                                           | sentence_1                                                                                                                                                                                                                                                                                                                                                                                |
  |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>A noir thriller set in Miami, the film follows an enforcer who discovers his femme fatale boss has branched out into cyber sex trafficking, putting a young runaway he’s befriended at risk. He sacrifices everything to save the young girl from the deadly organization he’s spent his life building.</code> | <code>Diabolik nearly gets caught in Inspector Ginko's latest trap, leaving his partner in crime Eva Kant behind in the escape. Furious, Eva offers Ginko her help in capturing the King of Terror, but the former has to face the return of an old flame of his.</code>                                                                                                                  |
  | <code>Deep inside the mountain of Dovre, something gigantic awakens after being trapped for a thousand years. Destroying everything in its path, the creature is fast approaching the capital of Norway. But how do you stop something you thought only existed in Norwegian folklore?</code>                        | <code>A fashion designer hires a nanny from the Philippines to assist her in caring for her family while she is suffering from what she believes is a tick-related illness. The nanny uses traditional Filipino folk healing techniques to help her, but in the process of doing so, she uncovers a horrifying truth about why she is there and why her employer is actually sick.</code> |
  | <code>Set in the Bronx during the tumultuous 1960s, an adolescent boy is torn between his honest, working-class father and a violent yet charismatic crime boss. Complicating matters is the youngster's growing attraction - forbidden in his neighborhood - for a beautiful black girl.</code>                     | <code>During the rise of fascism in Mussolini's Italy, a wooden boy brought magically to life struggles to live up to his father's expectations.</code>                                                                                                                                                                                                                                   |
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