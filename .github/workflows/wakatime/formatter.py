
class formatter:
    def format_progress_bar(self, percent):
        BAR_LEN = 25
        act = int(percent / (100/25))
        prog = '['
        prog += '=' * act
        prog += '.' * (BAR_LEN - act)
        prog += ']'
        return prog

    def format_array(self, elems, title = ''):
        fmt_arr = f'### {title}\n'

        fmt_arr += '```\n'
        cnt = 0
        for elem in elems:
            name = elem['name']
            time = elem['digital']
            percent = '%10.2f' % elem['percent']
            bar = self.format_progress_bar(elem['percent'])

            if name == 'Other':
                continue

            fmt_arr += f'{name.ljust(15)} {time.ljust(5)} {percent}% {bar}\n'
            cnt += 1

            if cnt >= 5:
                break

        fmt_arr+= '```\n'

        return fmt_arr

