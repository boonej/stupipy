def mit(year, holder):
    """Generates MIT License File

    :param year: Copyright year.
    :type year: String
    :param holder: Owner of copyright.
    :type holder: String

    """
    return (f'Copyright {year}, {holder}\n\n'
            'Permission is hereby granted, free of charge, to any person\n'
            'obtaining a copy of this software and associated documentation\n'
            'files (the "Software"), to deal in the Software without\n'
            'restriction, including without limitation the rights to use,\n'
            'copy, modify, merge, publish, distribute, sublicense, and/or\n'
            'sell copies of the Software, and to permit persons to whom the\n'
            'Software is furnished to do so, subject to the following\n'
            'conditions:\n\n'
            'The above copyright notice and this permission notice shall be\n'
            'included in all copies or substantial portions of the Software.\n'
            '\n'
            'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,\n'
            'EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES\n'
            'OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND\n'
            'NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT\n'
            'HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,\n'
            'WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING\n'
            'FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR\n'
            'OTHER DEALINGS IN THE SOFTWARE.')


def bsd(year, holder):
    return(f'Copyright {year}, {holder}\n\n'
           'Redistribution and use in source and binary forms, with or\n'
           'without modification, are permitted provided that the following\n'
           'conditions are met:\n\n'
           '1. Redistributions of source code must retain the above\n'
           'copyright notice, this list of conditions and the following\n'
           'disclaimer.\n'
           '2. Redistributions in binary form must reproduce the above\n'
           'copyright notice, this list of conditions and the following\n'
           'disclaimer in the documentation and / or other materials\n'
           'provided with the distribution.\n'
           '3. Neither the name of the copyright holder nor the names of its\n'
           'contributors may be used to endorse or promote products derived\n'
           'from this software without specific prior written permission.\n'
           'THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND\n'
           'CONTRIBUTORS \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES,\n'
           'INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF\n'
           'MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE\n'
           'DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR\n'
           'CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,\n'
           'SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES(INCLUDING, BUT NOT\n'
           'LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF\n'
           'USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED\n'
           'AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT\n'
           'LIABILITY, OR TORT(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN\n'
           'ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE\n'
           'POSSIBILITY OF SUCH DAMAGE.')
