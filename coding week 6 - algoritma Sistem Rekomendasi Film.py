import pandas as pd

# 1. Contoh dataset film
movies = pd.DataFrame({
    'title': [
        'Inception', 'The Dark Knight', 'Interstellar', 'Parasite', 
        'Joker', 'Avengers: Endgame', 'The Conjuring', 'Insidious', 
        'Toy Story', 'Coco', 'Hereditary', 'The Nun', 'Halloween', 'The Matrix'
    ],
    'genre': [
        'Sci-Fi, Action', 'Action, Crime, Drama', 'Sci-Fi, Drama', 'Thriller, Drama', 
        'Crime, Drama, Thriller', 'Action, Adventure, Sci-Fi', 'Horror, Mystery', 'Horror, Thriller',
        'Animation, Family', 'Animation, Adventure, Fantasy', 
        'Horror, Drama', 'Horror, Mystery, Thriller', 'Horror, Slasher', 'Sci-Fi, Action'
    ]
})

# 2. Fungsi untuk merekomendasikan film dari genre yang sama
def recommend_movies_based_on_genre(user_input_genre, movies):
    recommended_movies = movies[movies['genre'].str.contains(user_input_genre, case=False, na=False)]
    return recommended_movies[['title', 'genre']]

# 3. Loop interaktif dengan opsi reset genre
current_genre = None  # Awal tanpa genre
while True:
    if not current_genre:
        user_genre = input("\nMasukkan genre yang terakhir Anda tonton (atau ketik 'exit' untuk keluar): ").strip().lower()
        if user_genre == "exit":
            print("👋 Terima kasih telah menggunakan sistem rekomendasi!")
            break
        current_genre = user_genre  # Simpan genre saat ini

    # 4. Dapatkan rekomendasi berdasarkan genre
    recommendations = recommend_movies_based_on_genre(current_genre, movies)

    # 5. Cetak hasil rekomendasi
    if not recommendations.empty:
        print(f"\n🎬 Rekomendasi film dengan genre '{current_genre}':")
        print(recommendations.to_string(index=False))
    else:
        print(f"\n😢 Tidak ada film dengan genre '{current_genre}', coba genre lain!")
    
    # 6. Tanya user apakah ingin tetap di genre ini atau reset
    next_action = input("\nKetik 'reset' untuk mengganti genre atau Enter untuk lanjut: ").strip().lower()
    if next_action == "reset":
        current_genre = None  # Reset genre
