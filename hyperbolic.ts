const url = 'https://api.hyperbolic.xyz/v1/chat/completions';

const response = await fetch(url, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    Authorization: 'Bearer API Key',
  },
  body: JSON.stringify({
    model: 'Qwen/Qwen2.5-72B-Instruct',
    messages: [
      {
        role: 'user',
        content: 'What can I do in SF?'
      }
    ],
    max_tokens: 512,
    temperature: 0.7,
    top_p: 0.9,
    stream: false
  }),
});

const json = await response.json();

const output = json.choices[0].message.content;
console.log(output);
