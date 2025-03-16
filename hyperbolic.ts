import axios from 'axios';

const url = "https://api.hyperbolic.xyz/v1/chat/completions";
const headers = {
  "Content-Type": "application/json",
  "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJtYWxsaWNraGFzYW42NTFAZ21haWwuY29tIiwiaWF0IjoxNzQyMDA4NDQ4fQ.BNZ_w0CT-b7W-A2-WXcgyM6nrTxaF7bKmA1Glaj__Ss"
};

// Array of 100 questions
const questions: string[] = [
  "What's the best way to learn programming?",
  "How does quantum computing work?",
  "What are some healthy breakfast ideas?",
  "Can you explain blockchain technology?",
  "What's the weather like on Mars?",
  "How do I improve my photography skills?",
  "What are the benefits of meditation?",
  "How does artificial intelligence work?",
  "What's the history of the internet?",
  "Can you suggest some good books to read?",
  "What’s the meaning of life?",
  "How do I make a perfect cup of coffee?",
  "What are the latest space discoveries?",
  "How can I stay motivated to exercise?",
  "What’s the future of electric cars?",
  "How do I start a small business?",
  "What are some fun weekend activities?",
  "Can you explain the theory of relativity?",
  "What’s the best way to learn a language?",
  "How does the stock market work?",
  "What’s the best way to save money?",
  "How do I plan a trip abroad?",
  "What are the effects of climate change?",
  "How does Wi-Fi actually work?",
  "What’s the history of video games?",
  "How can I improve my public speaking?",
  "What’s the science behind rainbows?",
  "How do I grow indoor plants successfully?",
  "What are the benefits of drinking water?",
  "How does cryptocurrency mining work?",
  "What’s the history of chocolate?",
  "How can I reduce stress in my life?",
  "What are some tips for better sleep?",
  "How do solar panels generate electricity?",
  "What’s the best way to cook steak?",
  "How does the human brain process memory?",
  "What are some must-visit places in Europe?",
  "How do I start investing in stocks?",
  "What’s the difference between viruses and bacteria?",
  "How can I make my home more eco-friendly?",
  "What’s the history of the Olympic Games?",
  "How do I train a dog effectively?",
  "What are the benefits of yoga?",
  "How does 3D printing work?",
  "What’s the best way to learn guitar?",
  "How do airplanes stay in the air?",
  "What are some creative writing tips?",
  "How does the immune system fight diseases?",
  "What’s the future of space travel?",
  "How can I improve my time management?",
  "What’s the history of pizza?",
  "How do I create a budget?",
  "What are the benefits of recycling?",
  "How does virtual reality work?",
  "What’s the best way to study for exams?",
  "How do I make homemade bread?",
  "What are the causes of global warming?",
  "How does GPS technology work?",
  "What’s the history of photography?",
  "How can I boost my creativity?",
  "What are some tips for healthy eating?",
  "How do self-driving cars function?",
  "What’s the best way to learn cooking?",
  "How does the moon affect tides?",
  "What are some fun science experiments?",
  "How do I start a podcast?",
  "What’s the history of democracy?",
  "How can I improve my drawing skills?",
  "What are the benefits of journaling?",
  "How does nuclear energy work?",
  "What’s the best way to plan a party?",
  "How do I maintain a car properly?",
  "What are some tips for traveling cheap?",
  "How does the internet of things work?",
  "What’s the history of coffee?",
  "How can I learn to code faster?",
  "What are the benefits of team sports?",
  "How do black holes form?",
  "What’s the best way to declutter my home?",
  "How does machine learning differ from AI?",
  "What are some tips for gardening?",
  "How do I make a good first impression?",
  "What’s the history of the English language?",
  "How can I stay productive working from home?",
  "What are the benefits of learning history?",
  "How does the human eye see color?",
  "What’s the best way to train for a marathon?",
  "How do I start a blog?",
  "What are some unusual animal facts?",
  "How does sound travel through the air?",
  "What’s the history of fashion?",
  "How can I improve my negotiation skills?",
  "What are the benefits of mindfulness?",
  "How do I build a simple website?",
  "What’s the best way to learn math?",
  "How does evolution work?",
  "What are some tips for reducing waste?",
  "How do I choose a good wine?",
  "What’s the future of renewable energy?"
];

async function fetchAnswer(question: string): Promise<string> {
  const data = {
    messages: [
      {
        role: "user",
        content: question
      }
    ],
    model: "meta-llama/Llama-3.3-70B-Instruct",
    max_tokens: 512,
    temperature: 0.1,
    top_p: 0.9
  };

  try {
    const response = await axios.post(url, data, { headers });
    return response.data.choices[0].message.content || "No answer received";
  } catch (error) {
    console.error('Error fetching answer:', error);
    return "Error fetching answer.";
  }
}

function randomDelay(min: number, max: number): number {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

async function displayAnswers() {
  for (let i = 0; i < questions.length; i++) {
    console.log(`Question ${i + 1}: ${questions[i]}`);
    
    const answer = await fetchAnswer(questions[i]);
    console.log(`Answer: ${answer}`);
    
    // Simulate the pause between questions (60 to 120 seconds)
    const delay = randomDelay(60, 120) * 1000; // Convert seconds to milliseconds
    await new Promise(resolve => setTimeout(resolve, delay));
  }

  // Restart the 100 questions
  console.log("Restarting the cycle...");
  displayAnswers();
}

// Start the process
displayAnswers();
