from flask import Flask, render_template

app = Flask(__name__)

BOOKS = [
    {"title": "Trono de Vidro", "author": "Sarah J. Maas", "rating": "4.7", "cover": "book-01.webp", "synopsis": "Fantasia épica sobre uma assassina convocada para disputar sua liberdade em uma corte marcada por intrigas e poder."},
    {"title": "Jogos Vorazes", "author": "Suzanne Collins", "rating": "4.8", "cover": "book-02.jpg", "synopsis": "Em uma sociedade controlada por espetáculo e violência, uma jovem se torna símbolo de resistência e sobrevivência."},
    {"title": "A Guerra dos Tronos", "author": "George R. R. Martin", "rating": "4.8", "cover": "book-03.jpg", "synopsis": "Casas nobres disputam poder em um reino instável, onde alianças, honra e traição definem o destino de todos."},
    {"title": "Memórias Póstumas de Brás Cubas", "author": "Machado de Assis", "rating": "4.9", "cover": "book-04.png", "synopsis": "Clássico da literatura brasileira narrado por um defunto autor, com ironia refinada e crítica social precisa."},
    {"title": "Um Favorzinho do Vizinho", "author": "Catálogo contemporâneo", "rating": "4.2", "cover": "book-05.jpg", "synopsis": "Uma narrativa contemporânea sobre convivência, segredos de bairro e as consequências inesperadas de um pedido simples."},
    {"title": "O Caminho dos Reis", "author": "Brandon Sanderson", "rating": "4.9", "cover": "book-06.jpg", "synopsis": "Uma jornada monumental de honra, guerra e antigas ordens em um mundo de tempestades e escolhas decisivas."},
    {"title": "O Hobbit", "author": "J. R. R. Tolkien", "rating": "4.8", "cover": "book-07.jpg", "synopsis": "Bilbo Bolseiro parte em uma aventura inesperada que une coragem, amizade e a descoberta de um mundo grandioso."},
    {"title": "Odisseia", "author": "Homero", "rating": "4.7", "cover": "book-08.jpg", "synopsis": "Poema clássico sobre retorno, perseverança e astúcia, acompanhando Odisseu em sua longa viagem para casa."},
    {"title": "Mistborn", "author": "Brandon Sanderson", "rating": "4.8", "cover": "book-09.jpg", "synopsis": "Fantasia de sistemas mágicos sofisticados em um império opressor, onde uma rebelião nasce entre cinzas e metais."},
    {"title": "A Guerra da Papoula", "author": "R. F. Kuang", "rating": "4.6", "cover": "book-10.jpg", "synopsis": "Fantasia sombria inspirada em conflitos históricos, acompanhando poder, trauma e as escolhas difíceis da guerra."},
    {"title": "Alchemised", "author": "SenLinYu", "rating": "4.5", "cover": "book-11.jpg", "synopsis": "Romance de fantasia sombria com atmosfera intensa, disputas de poder e uma protagonista marcada por segredos."},
    {"title": "Torto Arado", "author": "Itamar Vieira Junior", "rating": "4.9", "cover": "book-12.jpg", "synopsis": "Romance brasileiro sobre terra, ancestralidade, trabalho e vínculos familiares no sertão da Bahia."},
    {"title": "A Metamorfose", "author": "Franz Kafka", "rating": "4.7", "cover": "book-13.png", "synopsis": "Uma obra essencial sobre estranhamento, isolamento e relações familiares, marcada por força simbólica e inquietação."},
    {"title": "Poder e Contrapoder na América Latina", "author": "Catálogo de ciências sociais", "rating": "4.4", "cover": "book-14.png", "synopsis": "Leitura crítica sobre disputas políticas, movimentos sociais e estruturas de poder no contexto latino-americano."},
    {"title": "O Jantar Secreto", "author": "Raphael Montes", "rating": "4.5", "cover": "book-15.jpg", "synopsis": "Suspense brasileiro de ritmo intenso sobre ambição, limites morais e decisões cada vez mais perigosas."},
    {"title": "As Veias Abertas da América Latina", "author": "Eduardo Galeano", "rating": "4.8", "cover": "book-16.jpg", "synopsis": "Ensaio histórico e político sobre exploração, dependência econômica e formação social da América Latina."},
    {"title": "Em Chamas", "author": "Suzanne Collins", "rating": "4.8", "cover": "book-17.jpg", "synopsis": "A continuação de Jogos Vorazes amplia a tensão política e transforma a sobrevivência em ato de resistência."},
    {"title": "A Esperança", "author": "Suzanne Collins", "rating": "4.7", "cover": "book-18.jpg", "synopsis": "Conclusão da trilogia, acompanhando os impactos da guerra, da propaganda e do preço pessoal da revolução."},
    {"title": "Império de Tempestades", "author": "Sarah J. Maas", "rating": "4.8", "cover": "book-19.jpg", "synopsis": "No universo de Trono de Vidro, alianças se intensificam enquanto antigos poderes definem o rumo da guerra."},
    {"title": "Dias Perfeitos", "author": "Raphael Montes", "rating": "4.4", "cover": "book-20.jpg", "synopsis": "Thriller psicológico brasileiro sobre obsessão, controle e os limites perturbadores de uma relação unilateral."},
]

@app.route("/")
def index():
    return render_template("index.html", books=BOOKS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


