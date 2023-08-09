from transformers import BloomForCausalLM
from transformers import BloomTokenizerFast


# 雲端 model
model = BloomForCausalLM.from_pretrained("bigscience/bloom-1b7")
tokenizer = BloomTokenizerFast.from_pretrained("bigscience/bloom-1b7")

# 給輸入字串和預期字數，返回結果
def gen(prompt, result_length):
    inputs = tokenizer(prompt, return_tensors="pt")
    return tokenizer.decode(model.generate(inputs["input_ids"],
                           max_length=result_length,
                           num_beams=2,
                           no_repeat_ngram_size=2,
                           early_stopping=True
                          )[0])

while True:
    prompt = input("prompt: ")
    length = int(input("length: "))
    result = gen(prompt, length)
    print(result)
