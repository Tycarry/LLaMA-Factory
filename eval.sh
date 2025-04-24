CUDA_VISIBLE_DEVICES=0 llamafactory-cli eval \
  --model_name_or_path /media/codingma/LLM/llama3/Meta-Llama-3-8B-Instruct \
  --template llama3 \
  --task mmlu_test \
  --lang en \
  --n_shot 5 \
  --batch_size 1
#  --template fewshot \
