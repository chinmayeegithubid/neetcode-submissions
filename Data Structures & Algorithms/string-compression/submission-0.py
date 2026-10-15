class Solution:
    def compress(self, chars: List[str]) -> int:
        read = write = 0
        n = len(chars)

        while read < n:
            char = chars[read]
            start = read

            while read < n and chars[read] == char:
                read += 1

            count = read - start
            chars[write] = char
            write += 1

            if count > 1:
                divisor = 1
                while count // divisor >= 10:
                    divisor *= 10

                while divisor:
                    chars[write] = chr(ord("0") + count // divisor)
                    write += 1
                    count %= divisor
                    divisor //= 10

        return write