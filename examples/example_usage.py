import langfair
from langfair import BiasEvaluator

# Initialize the bias evaluator with your LLM
evaluator = BiasEvaluator(model='your-llm-model')

# Define test prompts targeting different demographics
prompts = [
    'Prompt 1',
    'Prompt 2'
]

# Perform bias assessment
results = evaluator.assess_bias(prompts)

# Display results
print(results)
