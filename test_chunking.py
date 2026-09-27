from chunking import split_into_chunks 
with open (file='transcrib.txt',mode='r') as f:
    content = f.read()

chunks = split_into_chunks(content)
print(f'the number of chunks : {len(chunks)}')
for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i + 1} ---")
    print(chunk[:200])