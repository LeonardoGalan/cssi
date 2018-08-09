#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

def read_process_data():
    with open('third_party/jane-eyre.txt') as f:
        # the following line
        # - joins each line in the file into one big string
        # - removes all newlines and carriage returns
        # - converts everything to lowercase
        content = ' '.join(f.readlines()).replace('\n','').replace('\r','').lower()
        return content


# You do not need to call this function unless you are doing level 3
def get_stop_words():
    with open('stop-words.txt') as f:
        content = ' '.join(f.readlines()).replace('\n','').replace('\r','').lower()
        return content.split(' ')

def get_highest_words(counts_dictionary, count):
    highest = sorted(counts_dictionary.items(), key=lambda x:x[1])[::-1][:count]
    for word in highest:
        print("%s: %s" % (word[0], word[1]))


content = read_process_data()

# Write your solution below!
word_count={}

words = content.split(" ")

for word in words:
    if word_count.has_key(word):
        word_count[word] = word_count[word] + 1
    else:
        if word != "" and word not in stop_words:
        word_count[word] = 1

get_highest_words(word_count,10)

class Pet:
    '''
    _init__() is a method of the class Pet
    A method is a function that belongs to a classs instance. All methods of a class first
    parameter is self '''

    def _init_(self,name,age, animal = "dog"):
        '''self.name and self.age are instance attributes or data members of the class Pet.
        Instance attributes are unique in every occurrance (instance) of a Pet object'''

        self.name = name
        self.age = age
        self.animal = animal
        self.is_hunger = False
        self.mood = "happy"
def eat(self):
    self.is_hunger = False 
''' The pet class has the members age, name, count, __init()__self.
    To call the __init__() function we use the class name with the
    respective parameters within paranthesis'''



def
#o is an object of Pet
o = Pet ("Dog",3)


#t is another object of Pet
t = Pet("Cat",4)

print o.name, o.age, o.count
print t.name, t.age, t.count

t.count = 4

print o.name, o.age, o.count
print t.name, t.age, t.count
