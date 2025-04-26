import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if __name__ == "__main__":
    input_text = ' '.join(sys.argv[1:])
    validated_text = input_text.replace(' ', '%20')
    print(validated_text)
