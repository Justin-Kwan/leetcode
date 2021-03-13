import java.util.HashMap;
import java.util.ArrayList;

public class HelloWorld{
    
    // 1. reverse letters in a word (done)
    // 2. Reverse words in a sertence ()
    // 3. reverse words in a sentence but keep punctuation same

     public static void main(String []args){
        System.out.println(HelloWorld.reverseLettersIterate("hello"));
        
        System.out.println(HelloWorld.reverseWordsInSentence("Hello there I am coding."));

     }

    // + - * / 
    // time: O(N/2) = O(N) where N is number of letters
    // space: O(1)
    public static String reverseLettersIterate(String word) {
        int leftPtr = 0;
        int rightPtr = word.length() - 1;
        
        String [] chars = word.toCharArray();

        while (leftPtr < rightPtr) {
            char tempLeftChar = chars[leftPtr];

            chars[leftPtr] = chars[rightPtr];
            chars[rightPtr] = tempLeftChar;

            ++leftPtr;
            --rightPtr;
        }
        
        return new String(chars);
    }

    // assume that there is always a punctuation.
    // input: Hello ; there, I am coding.
    // output: Coding am, I there hello.
    // first-last
    // ["there,] -> ["there", ","]
    // time: O(N) where N is number of characters in sentence
    public static String reverseWordsInSentence(String sentence) {
        String[] words = sentence.split(" ");
        ArrayList<char> wordPunct = HelloWord.getPunctAtWordPos(words);

        int leftPtr = 0;
        int rightPtr = words.length - 1;

        while (leftPtr < rightPtr) {
            String tempLeftWord = words[leftPtr];

            words[leftPtr] = words[rightPtr];
            words[rightPtr] = tempLeftWord;

            ++leftPtr;
            --rightPtr;
        }

        if (words.length == 0) {
            return sentence;
        }

        // change first word's first letter to upper case.
        sentence = String.join(" ", words);
        char[] letters = sentence
            .toCharArray()
            .replaceAll("[.;?!,]", "")
            .toLowerCase();

        // make starting of sentence upper case
        letters[0] = Character.toUpperCase(letters[0]);
        sentence = new String(letters);

        return sentence;
    }

    // assumption: each word has 1 punctuation
    public static ArrayList<char> getPunctAtWordPos(String[] words) {
        ArrayList<char> punctInWords = new ArrayList<char>();

        Set<char> validPunct = new HashSet<char>();
        validPunct.add('.');
        validPunct.add(';');
        validPunct.add('?');
        validPunct.add('!');
        validPunct.add(',');

        for (int i = 0; i < words.length; ++i) {
            final char firstCharOfWord = words[i].getCharAt(0);
            final char lastCharOfWord = words[i].getCharAt(words[i].length - 1);
            
            final Boolean isPunctAtFront = validPunct.containsKey(firstCharOfWord);
            final Boolean isPunctAtBack = validPunct.containsKey(lastCharOfWord);

            if (isPunctAtFront) {
                punctInWords.add(firstCharOfWord);
                // could replace current word here...
            } else if (isPunctAtBack) {
                punctInWords.add(lastCharOfWord);
                // could replace current word here...
            }
        }

        return punctInWords;
    }
    
}