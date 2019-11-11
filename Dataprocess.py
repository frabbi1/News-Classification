from KeyWordExtractor import Vectorizer, KeywordExtractor


def make_corpus():

    print(len(KeywordExtractor.corpus))
    print(KeywordExtractor.corpus)


sport_words = KeywordExtractor("sports/").start_listing()
science_words = KeywordExtractor("scienceTech/").start_listing()
nat_words = KeywordExtractor("national/").start_listing()
int_words = KeywordExtractor("international/").start_listing()
ent_words = KeywordExtractor("entertainment/").start_listing()
bus_words = KeywordExtractor("business/").start_listing()

word_collection = sport_words.union(science_words.union(nat_words.union(int_words.union(ent_words.union(bus_words)))))

# print(word_collection)
# print(len(word_collection))
temp = list(word_collection)
words = sorted(temp)

# print(len(words))
# print(words)
#make_corpus()

vec = Vectorizer(words)
x = vec.vectorize(KeywordExtractor.corpus)
vec.tfidf(x)

# with open("all_words.txt", "a+") as word_file:
#     for word in words:
#
#         word_file.write(word)
#         word_file.write(" ")