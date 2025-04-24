CUDA_VISIBLE_DEVICES=0 API_PORT=8000 llamafactory-cli api \
    --model_name_or_path /model_file/Qwen1.5-4B/ \
    --adapter_name_or_path ./saves/qwen1.5-4b/lora/sft/ \
    --template qwen \
    --finetuning_type lora
