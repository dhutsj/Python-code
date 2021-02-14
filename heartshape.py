from wordcloud import WordCloud, STOPWORDS
import imageio
import matplotlib.pyplot as plt


def random_red_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None,
                          random_state=None):
    h = 0
    s = 100
    l = int(50 * (float(random_state.randint(60, 120)) / 100.0))
    return "hsl({}, {}%, {}%)".format(h, s, l)


def generate_word_cloud(words, image_file, saved_name):
    mask = imageio.imread(image_file)
    word_cloud = WordCloud(width=400,
                           height=400,
                           color_func=random_red_color_func,
                           background_color='white',
                           stopwords=STOPWORDS,
                           mask=mask).generate(words)
    plt.figure(figsize=(10, 8), facecolor='white', edgecolor='blue')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig(saved_name)

words = 'Paris, France, Vegas, Italy, America, Rome, Thailand, Seattle, Miami, London, Boston, Beijing, Shanghai, Korea, Moscow, Venice, Germany, Australia, Netherlands, Tokyo'
generate_word_cloud(words, 'heart.png', 'word_cloud.png')
