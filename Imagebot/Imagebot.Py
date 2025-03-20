import requests
import time
import random

# Your API URL and Headers
url = "https://api.hyperbolic.xyz/v1/image/generation"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_API_KEY_HERE"
}

# List of 100 prompts
prompts = [
    "Futuristic cityscape", 
    "A tranquil mountain view", 
    "A spaceship landing on Mars", 
    "A forest in autumn", 
    "Underwater scene with colorful fish", 
    "A fantasy castle", 
    "A cyberpunk city", 
    "A medieval knight", 
    "A tropical beach at sunset", 
    "A futuristic robot",
    "A bustling marketplace in an ancient city", 
    "A serene Japanese garden", 
    "An abandoned theme park", 
    "A majestic waterfall in the jungle", 
    "A dark wizard casting spells", 
    "A vibrant coral reef", 
    "A space station orbiting Earth", 
    "A dragon flying over a mountain range", 
    "A giant mechanical spider", 
    "A glowing city under the stars", 
    "A castle on the edge of a cliff", 
    "A deserted island with a lone palm tree", 
    "A cybernetic-enhanced human", 
    "An ancient temple hidden in the jungle", 
    "A steampunk airship", 
    "A neon-lit alleyway in a future metropolis", 
    "A medieval battle between knights", 
    "A wizard's library filled with ancient books", 
    "A haunted mansion on a foggy night", 
    "A giant robot fighting monsters", 
    "A lush rainforest filled with exotic animals", 
    "A futuristic city with flying cars", 
    "A pirate ship sailing through a storm", 
    "A vintage car on an open highway", 
    "A futuristic train traveling through a desert", 
    "A person walking through a snow-covered forest", 
    "A close-up of a rare exotic bird", 
    "A samurai warrior in full armor", 
    "A cat with cybernetic enhancements", 
    "A bustling futuristic port", 
    "A glowing portal in a dark cave", 
    "A tranquil beach at dawn", 
    "A moonlit night over a quiet village", 
    "A fiery explosion in space", 
    "A city submerged underwater", 
    "A giant, ancient oak tree", 
    "A post-apocalyptic wasteland", 
    "A futuristic skyscraper with solar panels", 
    "A colorful sunset over the ocean", 
    "A surreal dreamscape", 
    "A glowing moon over a futuristic city", 
    "A superhero flying over a city", 
    "A lone wolf in the snow", 
    "A spaceship traveling through a wormhole", 
    "A peaceful countryside with rolling hills", 
    "A giant mushroom forest", 
    "A retro 80s arcade", 
    "A glowing flower in a dark forest", 
    "A mystical creature in the mist", 
    "A bustling cyberpunk street", 
    "A robot tending to a garden", 
    "A fiery phoenix rising from the ashes", 
    "A waterfall with rainbow mist", 
    "A knight in shining armor on horseback", 
    "A spaceship docked on an alien planet", 
    "A hidden treasure chest in an underwater cave", 
    "A futuristic sports stadium", 
    "A grand piano in an elegant ballroom", 
    "A space explorer walking on an asteroid", 
    "A foggy forest path", 
    "A sleek, modern apartment overlooking a city", 
    "A group of astronauts on the Moon", 
    "A glowing jellyfish in deep ocean waters", 
    "A giant space telescope", 
    "A person meditating on top of a mountain", 
    "A gothic cathedral at night", 
    "A futuristic city with green technology", 
    "A time traveler in a Victorian city", 
    "A giant sand dune under a blue sky", 
    "A train station in the future", 
    "A mountain climber reaching the summit", 
    "A ninja performing a stealth move", 
    "A deserted spaceship in a barren landscape", 
    "A knight battling a dragon", 
    "A giant glowing crystal in a cave", 
    "A spaceship flying through an asteroid belt", 
    "A glowing city at night", 
    "A futuristic park with robots and greenery", 
    "A dragon made of fire", 
    "A mystical unicorn in a forest", 
    "A glowing moon over a quiet lake", 
    "A futuristic car speeding on a highway", 
    "A fantasy world with flying islands", 
    "A secret garden with glowing plants", 
    "A golden gate leading to a magical world", 
    "A giant whale swimming in space", 
    "A medieval castle surrounded by fog", 
    "A futuristic city with towering skyscrapers", 
    "A time machine in a laboratory", 
    "A robot playing chess with a human", 
    "A giant octopus in a deep-sea trench", 
    "A futuristic hovercraft", 
    "A huge library with ancient books", 
    "A person walking through a neon-lit city", 
    "A city built on floating islands", 
    "A glowing mountain under a starry sky", 
    "A medieval village at sunset", 
    "A creature from another dimension", 
    "A large asteroid passing by Earth", 
    "A spacecraft entering a distant galaxy", 
    "A surreal landscape with floating shapes", 
    "A lighthouse on a rocky shore", 
    "A glowing dragonfly hovering over a pond", 
    "A futuristic soldier in battle armor", 
    "A peaceful valley with a river", 
    "A robotic bird flying over the ocean"
]

# Loop through each prompt and make an API request
for i, prompt in enumerate(prompts, start=1):
    data = {
        "model_name": "SD1.5",
        "prompt": prompt,  # Use the specific prompt for each iteration
        "steps": 30,
        "cfg_scale": 5,
        "enable_refiner": False,
        "height": 1024,
        "width": 1024,
        "backend": "auto"
    }

    # Make the request to generate an image
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        response_data = response.json()
        # Print the full response for debugging
        print(response_data)

        # Extract the image URL (ensure the key is correct)
        image_url = response_data.get('image_url')  # Adjust key if needed
        if image_url:
            print(f"Image {i} URL: {image_url}")
        else:
            print(f"Error: Image URL not found in response for Image {i}.")
    else:
        print(f"Error: Failed to generate image {i}. Status Code: {response.status_code}")

    # Pause for a random interval between 60 and 120 seconds
    sleep_time = random.randint(60, 120)
    print(f"Pausing for {sleep_time} seconds...\n")
    time.sleep(sleep_time)

print("Completed generating all 100 images.")
