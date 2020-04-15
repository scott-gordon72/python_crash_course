chess_pieces = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']
print(f"There are {len(chess_pieces)} distinct chess pieces on the chess board")
print(f"Sorted pieces: {sorted(chess_pieces)}")
print(f"Reverse sorted pieces: {sorted(chess_pieces, reverse=True)}")
print(chess_pieces[0].title())