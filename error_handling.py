#position
class Position:
		def __init__(self, idx, ln, col, fn, ftxt):
				self.idx = idx
				self.ln = ln
				self.col = col
				self.fn = fn
				self.ftxt = ftxt

		def advance(self, current_char=None):
				self.idx += 1
				self.col += 1

				if current_char == '\n':
						self.ln += 1
						self.col = 0

				return self

		def copy(self):
				return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)

#######################################
# TOKENS
#######################################

TT_INT			= 'INT'
TT_FLOAT    = 'FLOAT'
TT_PLUS     = 'PLUS'
TT_MINUS    = 'MINUS'
TT_MUL      = 'MUL'
TT_DIV      = 'DIV'
TT_LPAREN   = 'LPAREN'
TT_RPAREN   = 'RPAREN'
TT_EOF			= 'EOF'




def string_with_arrows(text, pos_start, pos_end):
    result = ''

    # Calculate indices
    idx_start = max(text.rfind('\n', 0, pos_start.idx), 0)
    idx_end = text.find('\n', idx_start + 1)
    if idx_end < 0: idx_end = len(text)
    
    # Generate each line
    line_count = pos_end.ln - pos_start.ln + 1
    for i in range(line_count):
        # Calculate line columns
        line = text[idx_start:idx_end]
        col_start = pos_start.col if i == 0 else 0
        col_end = pos_end.col if i == line_count - 1 else len(line) - 1

        # Append to result
        result += line + '\n'
        result += ' ' * col_start + '^' * (col_end - col_start)

        # Re-calculate indices
        idx_start = idx_end
        idx_end = text.find('\n', idx_start + 1)
        if idx_end < 0: idx_end = len(text)

    return result.replace('\t', '')




class Error:
		def __init__(self, pos_start, pos_end, error_name, details):
				self.pos_start = pos_start
				self.pos_end = pos_end
				self.error_name = error_name
				self.details = details
		
		def as_string(self):
				result  = f'{self.error_name}: {self.details}\n'
				result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
				result += '\n\n' + string_with_arrows(self.pos_start.ftxt, self.pos_start, self.pos_end)
				return result

class IllegalCharError(Error):
		def __init__(self, pos_start, pos_end, details):
				super().__init__(pos_start, pos_end, 'Illegal Character', details)

class InvalidSyntaxError(Error):
		def __init__(self, pos_start, pos_end, details=''):
				super().__init__(pos_start, pos_end, 'Invalid Syntax', details)
pos_start = Position(1, 0, 0, 'filename.txt', 'Some code')
pos_end = Position(1, 5, 5, 'filename.txt', 'Some code')
error = IllegalCharError(pos_start, pos_end, "Invalid character: $")
print(error.as_string())
