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
- source_sentence: Elena and Ivan are getting ready to enter into a new phase in their
    life. They are leaving the metropolis of Barcelona to settle in the Catalan countryside,
    where they are taking over a cork oak plantation. Not only will the business pay
    for their living, but they also want to exploit the plantation equitably and sustainably.
    But despite their ideals, Elena and Ivan soon find themselves in a crisis which
    will endanger not only their project, but also their relationship.
  sentences:
  - 'This Christmas, Homer surprises Marge with the ultimate gift: an unforgettable
    performance from Italian opera superstar Andrea Bocelli and his children Matteo
    and Virginia.'
  - Nearly 5,000 years after he was bestowed with the almighty powers of the Egyptian
    gods—and imprisoned just as quickly—Black Adam is freed from his earthly tomb,
    ready to unleash his unique form of justice on the modern world.
  - The Red Ribbon Army, an evil organization that was once destroyed by Goku in the
    past, has been reformed by a group of people who have created new and mightier
    Androids, Gamma 1 and Gamma 2, and seek vengeance against Goku and his family.
- source_sentence: A female boxing trainer discovers that her champion cage-fighter
    boyfriend has been cheating on her with her sister and decides to seek revenge
    by training up his arch-rival to challenge him.
  sentences:
  - Kevin Hart - playing a version of himself - is on a death-defying quest to become
    an action star. And with a little help from John Travolta, Nathalie Emmanuel,
    and Josh Hartnett - he just might pull it off.
  - The Elric brothers’ long and winding journey comes to a close in this epic finale,
    where they must face off against an unworldly, nationwide threat.
  - Through a series of unfortunate events, three mummies end up in present-day London
    and embark on a wacky and hilarious journey in search of an old ring belonging
    to the Royal Family, stolen by ambitious archaeologist Lord Carnaby.
- source_sentence: Discover the game-changing partnership between a then undiscovered
    Michael Jordan and Nike's fledgling basketball division which revolutionized the
    world of sports and culture with the Air Jordan brand.
  sentences:
  - A journey deep into an uncharted and treacherous land, where fantastical creatures
    await the legendary Clades—a family of explorers whose differences threaten to
    topple their latest, and by far most crucial, mission.
  - Christopher Robin is headed off to college and he has abandoned his old friends,
    Pooh and Piglet, which then leads to the duo embracing their inner monsters.
  - Two sisters find an ancient book that gives birth to bloodthirsty demons that
    run amok in a Los Angeles apartment building and thrusts them into a primal battle
    for survival as they face the most nightmarish version of family imaginable.
- source_sentence: Christopher Robin is headed off to college and he has abandoned
    his old friends, Pooh and Piglet, which then leads to the duo embracing their
    inner monsters.
  sentences:
  - A sexual wellness company gains fame and followers, then members come forward
    with shocking allegations.
  - A gruesome serial killer is terrorizing London while brilliant but disgraced detective
    John Luther sits behind bars. Haunted by his failure to capture the cyber psychopath
    who now taunts him, Luther decides to break out of prison to finish the job by
    any means necessary.
  - After escaping a Michigan prison, a charming career criminal assumes a new identity
    in Canada and goes on to rob a record 59 banks and jewellery stores while being
    hunted by a rogue task force. Based on the story of The Flying Bandit.
- source_sentence: When Sheriff Roy Pulsipher finds himself in the afterlife, he joins
    a special police force and returns to Earth to save humanity from the undead.
  sentences:
  - A boy is given the ability to become an adult superhero in times of need with
    a single magic word.
  - After his retirement is interrupted by Gorr the God Butcher, a galactic killer
    who seeks the extinction of the gods, Thor Odinson enlists the help of King Valkyrie,
    Korg, and ex-girlfriend Jane Foster, who now wields Mjolnir as the Mighty Thor.
    Together they embark upon a harrowing cosmic adventure to uncover the mystery
    of the God Butcher’s vengeance and stop him before it’s too late.
  - After a catastrophic crash on an unknown planet, pilot Mills quickly discovers
    he's actually stranded on Earth…65 million years ago. Now, with only one chance
    at rescue, Mills and the only other survivor, Koa, must make their way across
    an unknown terrain riddled with dangerous prehistoric creatures in an epic fight
    to survive.
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
    'When Sheriff Roy Pulsipher finds himself in the afterlife, he joins a special police force and returns to Earth to save humanity from the undead.',
    "After a catastrophic crash on an unknown planet, pilot Mills quickly discovers he's actually stranded on Earth…65 million years ago. Now, with only one chance at rescue, Mills and the only other survivor, Koa, must make their way across an unknown terrain riddled with dangerous prehistoric creatures in an epic fight to survive.",
    'A boy is given the ability to become an adult superhero in times of need with a single magic word.',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.2702, 0.1930],
#         [0.2702, 1.0000, 0.1278],
#         [0.1930, 0.1278, 1.0000]])
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
  | details | <ul><li>min: 18 tokens</li><li>mean: 58.72 tokens</li><li>max: 129 tokens</li></ul> | <ul><li>min: 18 tokens</li><li>mean: 56.56 tokens</li><li>max: 129 tokens</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                            | sentence_1                                                                                                                                                                                                                                                                                                                                                                                                                                            |
  |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>Determined to prove the possibility of alternate dimensions, a graduate student unknowingly unlocks a gateway to unimaginable horror. Based on the H.P. Lovecraft's short story The Dreams in the Witch House.</code>                           | <code>After participating in a séance, young Laura begins to behave strangely. Alarmed, her parents ask Father Olmedo, one of the few exorcists authorized by the Vatican to intervene in cases of demonic possession, for help.</code>                                                                                                                                                                                                               |
  | <code>Sayen is hunting down the men who murdered her grandmother. Using her training and knowledge of nature, she is able to turn the tables on them, learning of a conspiracy from a corporation that threatens her people's ancestral lands.</code> | <code>Blindsided by a new generation of blazing-fast racers, the legendary Lightning McQueen is suddenly pushed out of the sport he loves. To get back in the game, he will need the help of an eager young race technician with her own plan to win, inspiration from the late Fabulous Hudson Hornet, and a few unexpected turns. Proving that #95 isn't through yet will test the heart of a champion on Piston Cup Racing’s biggest stage!</code> |
  | <code>Through a series of unfortunate events, three mummies end up in present-day London and embark on a wacky and hilarious journey in search of an old ring belonging to the Royal Family, stolen by ambitious archaeologist Lord Carnaby.</code>   | <code>After finding a host body in investigative reporter Eddie Brock, the alien symbiote must face a new enemy, Carnage, the alter ego of serial killer Cletus Kasady.</code>                                                                                                                                                                                                                                                                        |
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