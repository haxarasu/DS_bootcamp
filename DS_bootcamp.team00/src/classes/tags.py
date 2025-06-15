import csv

class Tags:
    def __init__(self, path_to_the_file):
        with open(path_to_the_file, "r") as file:
            read = csv.DictReader(file)
            self.data = [row for row in read]

            
    def most_words(self, n):
        tag_word_count = {}

        for row in self.data:
            tag = row["tag"]
            word_count = len(tag.split())
            if tag not in tag_word_count:
                tag_word_count[tag] = word_count

        sorted_tags = sorted(tag_word_count.items(), key=lambda item: item[1], reverse=True)
        
        big_tags = dict(sorted_tags[:n])
    
        return big_tags
    
    
    def longest(self, n):
        tag_length = {}

        for row in self.data:
            tag = row["tag"]
            length = len(tag)
            if tag not in tag_length:
                tag_length[tag] = length

        sorted_tags = sorted(tag_length.items(), key=lambda item: item[1], reverse=True)

        big_tags = [tag for tag, _ in sorted_tags[:n]]
    
        return big_tags


    def most_words_and_longest(self, n):
        most_words = {row['tag']: len(row['tag'].split()) for row in self.data}
        top_most_words = set(dict(sorted(most_words.items(), key=lambda item: item[1], reverse=True)[:n]))

        longest_tags = {row['tag']: len(row['tag']) for row in self.data}
        top_longest_tags = set(dict(sorted(longest_tags.items(), key=lambda item: item[1], reverse=True)[:n]))

        return list(top_most_words & top_longest_tags)


    def most_popular(self, n):
        tag_count = {}

        for row in self.data:
            tag = row["tag"]
            if tag not in tag_count:
                tag_count[tag] = 1
            else:
                tag_count[tag] += 1

        sorted_tags = sorted(tag_count.items(), key=lambda item: item[1], reverse=True)
        
        popular_tags = dict(sorted_tags[:n])
    
        return popular_tags
    

    def tags_with(self, word):
        unique_tags = set()

        word = word.lower()

        for row in self.data:
            tag = row["tag"].lower()
            if word in tag:
                unique_tags.add(row["tag"])

        tags_with_word = sorted(unique_tags)

        return tags_with_word