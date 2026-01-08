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
- source_sentence: Shanghai, 1934. In an insect world parallel to that of humans,
    veteran Inspector Sun, a lone spider, leads his last mission against his archenemy
    the Red Locust, before embarking on a well-deserved retirement. His vacation aboard
    a Pan Am clipper between Shanghai and San Francisco comes to an abrupt end when
    millionaire Dr. Spindelthorp is found murdered. What begins as a routine case
    for Sun will ultimately decide the fate of humanity.
  sentences:
  - After old enemies kill his family, a former mafia enforcer and his feisty daughter
    flee to Milan, where they hide out while plotting their revenge.
  - After finding a host body in investigative reporter Eddie Brock, the alien symbiote
    must face a new enemy, Carnage, the alter ego of serial killer Cletus Kasady.
  - After starting their own detective agency, Nick and Audrey Spitz land a career-making
    case when their billionaire pal is kidnapped from his wedding.
- source_sentence: Ryan Logan, a former Special Forces operative, is battling to cope
    with life after the loss of his wife.  He is thrusted into the criminal underworld
    to keep his only son from being taken from him.
  sentences:
  - An aging Chinese immigrant is swept up in an insane adventure, where she alone
    can save what's important to her by connecting with the lives she could have led
    in other universes.
  - Harry Potter has lived under the stairs at his aunt and uncle's house his whole
    life. But on his 11th birthday, he learns he's a powerful wizard—with a place
    waiting for him at the Hogwarts School of Witchcraft and Wizardry. As he learns
    to harness his newfound powers with the help of the school's kindly headmaster,
    Harry uncovers the truth about his parents' deaths—and about the villain who's
    to blame.
  - An aging Chinese immigrant is swept up in an insane adventure, where she alone
    can save what's important to her by connecting with the lives she could have led
    in other universes.
- source_sentence: 'Mathieu, a member of the French institute in Irkutsk, is arrested
    overnight by the Russian authorities.  Imprisoned and accused of sexual abuse
    on his own daughter, he realises he is a victim of a Kompromat. With the help
    of the FSB, someone has built up a case to frame him. Isolated, he has no one
    to turn to. Proving his innocence is impossible: the only solution is to escape.'
  sentences:
  - Ophelia, a young nun recently arriving in the town of San Ramon, is forced to
    perform an exorcism on a pregnant woman in danger of dying. Just when she thinks
    her possession has ended, she discovers that the evil presence hasn't disappeared
    yet. The director of the award-winning Here Comes the Devil and Late Phases adds
    a new twist to possession movies in one of this year's Latin American horror surprises.
  - The Red Ribbon Army, an evil organization that was once destroyed by Goku in the
    past, has been reformed by a group of people who have created new and mightier
    Androids, Gamma 1 and Gamma 2, and seek vengeance against Goku and his family.
  - A young girl discovers an idealized parallel universe behind a secret door in
    her new home, unaware that it contains a sinister secret.
- source_sentence: 'Blindsided by a new generation of blazing-fast racers, the legendary
    Lightning McQueen is suddenly pushed out of the sport he loves. To get back in
    the game, he will need the help of an eager young race technician with her own
    plan to win, inspiration from the late Fabulous Hudson Hornet, and a few unexpected
    turns. Proving that #95 isn''t through yet will test the heart of a champion on
    Piston Cup Racing’s biggest stage!'
  sentences:
  - All Gary wants is to make awesome home movies with his best buds. All his older
    sister Samantha wants is to hang with the cool kids. When their parents head out
    of town one Halloween weekend, an all-time rager of a teen house party turns to
    terror when aliens attack, forcing the siblings to band together to survive the
    night.
  - It has been a year since Mic Mic and Oscar returned from their incredible adventure.
    And now, after a diabolical plan by Vulture to sabotage the delivery of the Grizzly
    cub to his opponent in the American presidential elections, Mic Mic, Oscar, Panda
    teenager and Stork set off on another great adventure as they ride a zeppelin
    to return little Grizzly to its rightful parents and save the American elections
    and the whole continent from an erupting volcano.
  - While working underground to fix a water main, Brooklyn plumbers—and brothers—Mario
    and Luigi are transported down a mysterious pipe and wander into a magical new
    world. But when the brothers are separated, Mario embarks on an epic quest to
    find Luigi.
- source_sentence: 'Puss in Boots discovers that his passion for adventure has taken
    its toll: He has burned through eight of his nine lives, leaving him with only
    one life left. Puss sets out on an epic journey to find the mythical Last Wish
    and restore his nine lives.'
  sentences:
  - Through a series of unfortunate events, three mummies end up in present-day London
    and embark on a wacky and hilarious journey in search of an old ring belonging
    to the Royal Family, stolen by ambitious archaeologist Lord Carnaby.
  - A gruesome serial killer is terrorizing London while brilliant but disgraced detective
    John Luther sits behind bars. Haunted by his failure to capture the cyber psychopath
    who now taunts him, Luther decides to break out of prison to finish the job by
    any means necessary.
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
    'Puss in Boots discovers that his passion for adventure has taken its toll: He has burned through eight of his nine lives, leaving him with only one life left. Puss sets out on an epic journey to find the mythical Last Wish and restore his nine lives.',
    'Elena and Ivan are getting ready to enter into a new phase in their life. They are leaving the metropolis of Barcelona to settle in the Catalan countryside, where they are taking over a cork oak plantation. Not only will the business pay for their living, but they also want to exploit the plantation equitably and sustainably. But despite their ideals, Elena and Ivan soon find themselves in a crisis which will endanger not only their project, but also their relationship.',
    'Through a series of unfortunate events, three mummies end up in present-day London and embark on a wacky and hilarious journey in search of an old ring belonging to the Royal Family, stolen by ambitious archaeologist Lord Carnaby.',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.1894, 0.2391],
#         [0.1894, 1.0000, 0.1800],
#         [0.2391, 0.1800, 1.0000]])
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
  | details | <ul><li>min: 18 tokens</li><li>mean: 58.72 tokens</li><li>max: 129 tokens</li></ul> | <ul><li>min: 18 tokens</li><li>mean: 58.42 tokens</li><li>max: 129 tokens</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                                                                                                                           | sentence_1                                                                                                                                                                                                                                                                                                                             |
  |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>A cold and mysterious new security guard for a Los Angeles cash truck company surprises his co-workers when he unleashes precision skills during a heist. The crew is left wondering who he is and where he came from. Soon, the marksman's ultimate motive becomes clear as he takes dramatic and irrevocable steps to settle a score.</code> | <code>With the price on his head ever increasing, John Wick uncovers a path to defeating The High Table. But before he can earn his freedom, Wick must face off against a new enemy with powerful alliances across the globe and forces that turn old friends into foes.</code>                                                        |
  | <code>Puss in Boots discovers that his passion for adventure has taken its toll: He has burned through eight of his nine lives, leaving him with only one life left. Puss sets out on an epic journey to find the mythical Last Wish and restore his nine lives.</code>                                                                              | <code>A young girl discovers an idealized parallel universe behind a secret door in her new home, unaware that it contains a sinister secret.</code>                                                                                                                                                                                   |
  | <code>A mysterious force knocks the moon from its orbit around Earth and sends it hurtling on a collision course with life as we know it.</code>                                                                                                                                                                                                     | <code>After depleting Earth's resources for centuries, humankind's survival requires an exodus to outer space. An international expedition is quickly formed to find a suitable new planet, but when plans go awry, the crew is suddenly stranded without power on a strange planet, where something unimaginable lies in wait.</code> |
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