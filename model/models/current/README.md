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
- source_sentence: Unlucky assassin Ladybug is determined to do his job peacefully
    after one too many gigs gone off the rails. Fate, however, may have other plans,
    as Ladybug's latest mission puts him on a collision course with lethal adversaries
    from around the globe—all with connected, yet conflicting, objectives—on the world's
    fastest train.
  sentences:
  - When Harry Potter's name emerges from the Goblet of Fire, he becomes a competitor
    in a grueling battle for glory among three wizarding schools—the Triwizard Tournament.
    But since Harry never submitted his name for the Tournament, who did? Now Harry
    must confront a deadly dragon, fierce water demons and an enchanted maze only
    to find himself in the cruel grasp of He Who Must Not Be Named.
  - Set in the Bronx during the tumultuous 1960s, an adolescent boy is torn between
    his honest, working-class father and a violent yet charismatic crime boss. Complicating
    matters is the youngster's growing attraction - forbidden in his neighborhood
    - for a beautiful black girl.
  - When a lively young family moves in next door, grumpy widower Otto Anderson meets
    his match in a quick-witted, pregnant woman named Marisol, leading to an unlikely
    friendship that turns his world upside down.
- source_sentence: In 1988, American video game salesman Henk Rogers discovers the
    video game Tetris. When he sets out to bring the game to the world, he enters
    a dangerous web of lies and corruption behind the Iron Curtain.
  sentences:
  - John Wick is forced out of retirement by a former associate looking to seize control
    of a shadowy international assassins’ guild. Bound by a blood oath to aid him,
    Wick travels to Rome and does battle against some of the world’s most dangerous
    killers.
  - Valeria's joy at becoming a first-time mother is quickly taken away when she's
    cursed by a sinister entity. As danger closes in, she's forced deeper into a chilling
    world of dark magic that threatens to consume her.
  - All Gary wants is to make awesome home movies with his best buds. All his older
    sister Samantha wants is to hang with the cool kids. When their parents head out
    of town one Halloween weekend, an all-time rager of a teen house party turns to
    terror when aliens attack, forcing the siblings to band together to survive the
    night.
- source_sentence: After his retirement is interrupted by Gorr the God Butcher, a
    galactic killer who seeks the extinction of the gods, Thor Odinson enlists the
    help of King Valkyrie, Korg, and ex-girlfriend Jane Foster, who now wields Mjolnir
    as the Mighty Thor. Together they embark upon a harrowing cosmic adventure to
    uncover the mystery of the God Butcher’s vengeance and stop him before it’s too
    late.
  sentences:
  - 'This Christmas, Homer surprises Marge with the ultimate gift: an unforgettable
    performance from Italian opera superstar Andrea Bocelli and his children Matteo
    and Virginia.'
  - Nearly 5,000 years after he was bestowed with the almighty powers of the Egyptian
    gods—and imprisoned just as quickly—Black Adam is freed from his earthly tomb,
    ready to unleash his unique form of justice on the modern world.
  - A semi-retired special ops assassin and a DEA agent cross paths on separate missions
    to stop a cyber terrorist organization that has built a dangerous machine threatening
    to attack the power grid and bring catastrophe to the world.
- source_sentence: Reporters Loretta McLaughlin and Jean Cole bravely pursue the story
    of the Boston Strangler at great personal risk, putting their own lives on the
    line in their quest to uncover the truth.
  sentences:
  - A stubborn and hotheaded minor league basketball coach is forced to train a Special
    Olympics team when he is sentenced to community service.
  - The Red Ribbon Army, an evil organization that was once destroyed by Goku in the
    past, has been reformed by a group of people who have created new and mightier
    Androids, Gamma 1 and Gamma 2, and seek vengeance against Goku and his family.
  - In his second year of fighting crime, Batman uncovers corruption in Gotham City
    that connects to his own family while facing a serial killer known as the Riddler.
- source_sentence: A semi-retired special ops assassin and a DEA agent cross paths
    on separate missions to stop a cyber terrorist organization that has built a dangerous
    machine threatening to attack the power grid and bring catastrophe to the world.
  sentences:
  - Explorer Bruce Wayne accidentally unleashes an ancient evil, and returns to Gotham
    after being away for two decades. There, Batman battles Lovecraftian supernatural
    forces and encounters allies and enemies such as Green Arrow, Ra's al Ghul, Mr.
    Freeze, Killer Croc, Two-Face and James Gordon.
  - John Wick is forced out of retirement by a former associate looking to seize control
    of a shadowy international assassins’ guild. Bound by a blood oath to aid him,
    Wick travels to Rome and does battle against some of the world’s most dangerous
    killers.
  - Elena and Ivan are getting ready to enter into a new phase in their life. They
    are leaving the metropolis of Barcelona to settle in the Catalan countryside,
    where they are taking over a cork oak plantation. Not only will the business pay
    for their living, but they also want to exploit the plantation equitably and sustainably.
    But despite their ideals, Elena and Ivan soon find themselves in a crisis which
    will endanger not only their project, but also their relationship.
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
    'A semi-retired special ops assassin and a DEA agent cross paths on separate missions to stop a cyber terrorist organization that has built a dangerous machine threatening to attack the power grid and bring catastrophe to the world.',
    'Elena and Ivan are getting ready to enter into a new phase in their life. They are leaving the metropolis of Barcelona to settle in the Catalan countryside, where they are taking over a cork oak plantation. Not only will the business pay for their living, but they also want to exploit the plantation equitably and sustainably. But despite their ideals, Elena and Ivan soon find themselves in a crisis which will endanger not only their project, but also their relationship.',
    "Explorer Bruce Wayne accidentally unleashes an ancient evil, and returns to Gotham after being away for two decades. There, Batman battles Lovecraftian supernatural forces and encounters allies and enemies such as Green Arrow, Ra's al Ghul, Mr. Freeze, Killer Croc, Two-Face and James Gordon.",
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.1028, 0.2409],
#         [0.1028, 1.0000, 0.0764],
#         [0.2409, 0.0764, 1.0000]])
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
  |         | sentence_0                                                                          | sentence_1                                                                         |
  |:--------|:------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
  | type    | string                                                                              | string                                                                             |
  | details | <ul><li>min: 18 tokens</li><li>mean: 58.72 tokens</li><li>max: 129 tokens</li></ul> | <ul><li>min: 18 tokens</li><li>mean: 56.7 tokens</li><li>max: 129 tokens</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                                                                                                                                                                        | sentence_1                                                                                                                                                                                                                                                                                                                                                                    |
  |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>This Christmas, Homer surprises Marge with the ultimate gift: an unforgettable performance from Italian opera superstar Andrea Bocelli and his children Matteo and Virginia.</code>                                                                                                                                                                                                         | <code>Escaping death, a Hebrew infant is raised in a royal household to become a prince. Upon discovery of his true heritage, Moses embarks on a personal quest to reclaim his destiny as the leader and liberator of the Hebrew people.</code>                                                                                                                               |
  | <code>Tanjiro finds his family slaughtered and the lone survivor, his sister Nezuko Kamado, turned into a Demon. To his surprise, however, Nezuko still shows signs of human emotion and thought. Thus begins Tanjiro's journey to seek out the Demon who killed their family and turn his sister human again. A recap film of Kimetsu no Yaiba, covering episodes 1-5 with extra footage.</code> | <code>Set in the Bronx during the tumultuous 1960s, an adolescent boy is torn between his honest, working-class father and a violent yet charismatic crime boss. Complicating matters is the youngster's growing attraction - forbidden in his neighborhood - for a beautiful black girl.</code>                                                                              |
  | <code>Escaping death, a Hebrew infant is raised in a royal household to become a prince. Upon discovery of his true heritage, Moses embarks on a personal quest to reclaim his destiny as the leader and liberator of the Hebrew people.</code>                                                                                                                                                   | <code>Tanjiro Kamado, joined with Inosuke Hashibira, a boy raised by boars who wears a boar's head, and Zenitsu Agatsuma, a scared boy who reveals his true power when he sleeps, boards the Infinity Train on a new mission with the Fire Hashira, Kyojuro Rengoku, to defeat a demon who has been tormenting the people and killing the demon slayers who oppose it!</code> |
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