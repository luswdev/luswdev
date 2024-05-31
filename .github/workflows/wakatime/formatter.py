
class formatter:
    def format_progress_bar(self, percent):
        BAR_LEN = 32
        act = int(percent / (100/25))
        prog = '['
        prog += '=' * act
        prog += '.' * (BAR_LEN - act)
        prog += ']'
        return prog

    def format_array(self, elems, title = ''):
        fmt_arr = f'### {title}\n<br/>'

        fmt_arr += '```\n'
        cnt = 0
        for elem in elems:
            name = elem['name']
            time = elem['text']
            percent = '%8.2f' % elem['percent']
            bar = self.format_progress_bar(elem['percent'])

            if name == 'Other':
                continue

            fmt_arr += f'{name.ljust(15)} {time.rjust(15)}   {bar} {percent}%\n'
            cnt += 1

            if cnt >= 5:
                break

        fmt_arr+= '```\n'

        return fmt_arr

