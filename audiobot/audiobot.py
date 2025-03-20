import requests
import time
import random
import os

# Define the API endpoint and headers
url = "https://api.hyperbolic.xyz/v1/audio/generation"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_API_KEY_HERE"  # Replace with your actual API key
}

# List of text phrases to use for audio generation (expanded to 100 items)
texts = [
    "Los Angeles! The City of Angels is a treasure trove of exciting experiences, iconic landmarks, and endless entertainment options.",
    "Explore the beaches, Hollywood, and the beautiful sun-kissed weather that Los Angeles has to offer.",
    "The Hollywood Sign, Griffith Observatory, and Universal Studios are just a few of the amazing attractions you'll find in Los Angeles.",
    "Los Angeles is not just a city; it's a world of diverse cultures, innovation, and endless creativity.",
    "From the bustling streets of Downtown LA to the serene beauty of Malibu, Los Angeles offers something for everyone.",
    "Did you know that Los Angeles is home to some of the world's most famous museums, including The Getty Center and LACMA?",
    "Los Angeles is a global hub for entertainment, fashion, and technology, making it one of the most exciting cities in the world.",
    "Los Angeles is also known for its vibrant nightlife, offering endless options for those who love to explore after dark.",
    "Take a stroll along the Santa Monica Pier or shop on Rodeo Drive—Los Angeles has something for every taste.",
    "Whether you're a fan of the arts or an adrenaline junkie, LA has a variety of museums, theaters, parks, and sports arenas.",
    "The city boasts the iconic Venice Beach, where you can enjoy the sun, the sand, and a unique cultural vibe.",
    "From its world-famous film industry to the heart of tech innovation in Silicon Beach, LA is at the crossroads of creativity and industry.",
    "Los Angeles is a cultural melting pot, with diverse communities and a mix of traditions from all around the world.",
    "The food scene in LA is just as diverse, offering everything from gourmet dining to delicious street food and everything in between.",
    "Los Angeles is home to a wide variety of outdoor activities, from hiking in the hills to surfing on the Pacific coastline.",
    "LA’s downtown area is a vibrant, ever-evolving neighborhood, filled with art galleries, music venues, and trendy restaurants.",
    "With an endless list of events, festivals, and outdoor activities, Los Angeles is always buzzing with excitement.",
    "Hollywood is the epicenter of the global entertainment industry, with thousands of visitors flocking to experience its magic every year.",
    "Whether you're visiting the Walt Disney Concert Hall or attending a live TV show, LA's cultural and artistic offerings are second to none.",
    "Don't forget the stunning architecture, from the historic Olvera Street to the modern structures of downtown LA.",
    "Los Angeles is a city that never sleeps, with its streets always full of life, creativity, and energy, day and night.",
    "The Los Angeles International Airport (LAX) is one of the busiest airports in the world, bringing people from all over the globe.",
    "If you're a car enthusiast, you'll love the Southern California car culture, from classic car shows to automotive museums.",
    "Los Angeles has a long history of being a creative haven, with filmmakers, musicians, and artists calling it home for generations.",
    "Did you know LA has over 100 miles of coastline, including stunning beaches like Malibu, Venice Beach, and Manhattan Beach?",
    "Los Angeles also has a large LGBTQ+ community, with a wide range of events, resources, and businesses supporting diversity and inclusion.",
    "Take a tour of the Los Angeles County Museum of Art (LACMA), which holds an impressive collection of art from all over the world.",
    "Visit the famous La Brea Tar Pits, where you can see the ancient fossils of prehistoric animals trapped in the tar.",
    "The Los Angeles Botanical Garden offers a serene escape from the city, with beautifully landscaped gardens and scenic walking paths.",
    "From its gorgeous weather to its world-class shopping and dining options, Los Angeles truly has something for everyone.",
    "Don't forget to visit the Griffith Park Observatory, offering both stunning views of the city and fascinating exhibits about the stars.",
    "If you're a sports fan, LA is home to multiple championship-winning teams like the Lakers, Dodgers, and Rams.",
    "The city has been featured in countless movies and TV shows, making it an iconic backdrop for the entertainment industry.",
    "Whether you’re into hiking, biking, or simply enjoying nature, Los Angeles offers countless parks, trails, and scenic viewpoints.",
    "Los Angeles is also known for its incredible street art scene, with murals and installations lining many of its urban streets.",
    "For those who love shopping, LA offers everything from high-end boutiques on Melrose Avenue to bargain hunting at the Santee Alley.",
    "Los Angeles has a long-standing tradition of artistic and musical innovation, being the birthplace of countless trends and movements.",
    "The diversity in LA also brings a wide range of cultural festivals, including celebrations of everything from food to art and music.",
    "One of the most famous landmarks in LA is the Venice Beach Boardwalk, known for its eclectic mix of street performers, vendors, and artists.",
    "A trip to Los Angeles wouldn’t be complete without seeing the iconic Sunset Boulevard, stretching through Hollywood and Beverly Hills.",
    "If you're a nature lover, you'll enjoy the easy access to hiking spots such as Runyon Canyon or the Angeles National Forest.",
    "The nightlife in Los Angeles is unparalleled, with rooftop bars, trendy nightclubs, and intimate venues offering entertainment all night long.",
    "Los Angeles is also home to a thriving tech industry, with Silicon Beach becoming a major hub for startups and tech giants.",
    "From watching live performances at The Greek Theatre to attending an open-air concert at Hollywood Bowl, LA is a musical paradise.",
    "Every year, Los Angeles hosts the Academy Awards, bringing together the biggest stars and celebrating the world’s best film talent.",
    "Los Angeles is a city of innovators, where new ideas are born, whether in tech, fashion, or the entertainment industry.",
    "The natural beauty of Los Angeles is unmatched, with sprawling beaches, towering mountains, and scenic desert landscapes all nearby.",
    "Take a trip to the Natural History Museum of Los Angeles County to explore exhibits showcasing everything from dinosaurs to ancient cultures.",
    "Los Angeles is a beacon of opportunity, attracting talent from around the world, whether in entertainment, business, or the arts.",
    "With its sunny weather, diverse culture, and endless attractions, Los Angeles is a must-see destination for travelers from around the globe.",
    "Whether you’re a movie buff, an art enthusiast, or a thrill-seeker, Los Angeles is a city where dreams come true.",
    "Los Angeles is home to some of the best universities and institutions, including UCLA and the University of Southern California (USC).",
    "From its impressive skylines to its quiet residential neighborhoods, Los Angeles offers a balance of city life and suburban comfort.",
    "Los Angeles is a popular destination for both tourists and locals, offering everything from iconic landmarks to hidden gems off the beaten path."
] * 2  # This will give us 100 texts (50 phrases * 2 = 100 total)

def generate_audio(index, text):
    try:
        # Data for the request, using the current text
        data = {
            "text": text,
            "speed": 1
        }

        # Send POST request to the API
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise error for bad status codes

        # Check if the response is in the expected format
        if response.status_code == 200:
            audio_content = response.content
            print(f"Audio {index} generated successfully.")
            
            # Save the audio to a file with an incremental name
            file_name = f"output_audio_{index}.mp3"
            with open(file_name, "wb") as audio_file:
                audio_file.write(audio_content)
            print(f"Audio saved as {file_name}")

        else:
            print(f"Failed to generate audio {index}. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error during the request for audio {index}: {e}")

# Main function to fetch 100 audios with random pause intervals
def fetch_multiple_audios():
    while True:  # Keep generating the audios indefinitely
        for i in range(1, 101):
            # Select the text from the list for this iteration
            text = texts[i-1]  # List is 0-indexed
            print(f"\nFetching audio {i} with text: {text[:50]}...")  # Print the first 50 characters of the text for clarity
            generate_audio(i, text)

            # Random pause between 60 and 120 seconds
            pause_duration = random.randint(60, 120)
            print(f"Pausing for {pause_duration} seconds...\n")
            time.sleep(pause_duration)  # Pause before generating the next audio

        print("Completed generating 100 audios. Restarting the process...\n")

if __name__ == "__main__":
    fetch_multiple_audios()
