from .. import loader
import operator, math


@loader.tds
class CalcMod(loader.Module):
    strings = {"name": "Cacl",
              "no_term": "<b>Нічого не знайдено</b>"}
    
    @loader.owner
    async def calccmd(self, message):
        text = utils.get_args_raw(message.message)
        if not text:
            text = (await message.get_reply_message()).message
        if not text:
            await utils.answer(message, self.strings("no_term", message))
            return
        OPS = {
            '-': operator.sub,
            '+': operator.add,
            '*': operator.mul,
            '/': operator.truediv,
        }
        FUNCS = {
            'sin': math.sin,
            'cos': math.cos,
        }

        def calc(token):
            try:
                return float(token)

            except ValueError:
                begin = token.find('(')
                if begin == 0 and token[-1] == ')':
                    return parse(token[1:-1])

                elif begin > 0 and token[-1] == ')':
                    name = token[0:begin]
                    if name not in FUNCS:
                        raise ValueError('Unknown function %s' % name)
                    result = FUNCS[name](parse(token[begin + 1:-1]))
                    return result

                else:
                    raise ValueError('Unknown token %s' % repr(token))

        def parse(txt):
            token = ''
            depth = 0
            op = None
            current_value = None

            def close_token():
                nonlocal token, op, current_value
                if token != '':
                    if current_value is None:
                        current_value = calc(token)
                    else:
                        current_value = OPS[op](current_value, calc(token))
                        op = None
                    print(op, token, current_value)
                    token = ''

            for c in txt:
                if depth > 0:
                    if c == ' ':
                        continue
                    token += c
                    if c == ')':
                        depth -= 1
                        close_token()

                elif c == '(':
                    if token == '':
                        close_token()
                    depth += 1
                    token += c

                else:
                    if c == ' ':
                        continue
                    elif c in OPS:
                        close_token()
                        op = c
                    else:
                        token += c

            close_token()
            return current_value
        
        await message.edit("COMMAND: " + text)
