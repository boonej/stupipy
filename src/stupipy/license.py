def mit(year, holder):
    """Generates MIT License File

    :param year: Copyright year.
    :type year: String
    :param holder: Copyright holder.
    :type holder: String
    :return: MIT license document.
    :rtype: String

    """
    return (
        f'Copyright {year}, {holder}\n\n'
        'Permission is hereby granted, free of charge, to any person\n'
        'obtaining a copy of this software and associated documentation\n'
        'files (the "Software"), to deal in the Software without\n'
        'restriction, including without limitation the rights to use, copy,\n'
        'modify, merge, publish, distribute, sublicense, and/or sell copies\n'
        'of the Software, and to permit persons to whom the Software is\n'
        'furnished to do so, subject to the following conditions:\n\n'
        'The above copyright notice and this permission notice shall be\n'
        'included in all copies or substantial portions of the Software.\n\n'
        'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,\n'
        'EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES\n'
        'OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND\n'
        'NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT\n'
        'HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,\n'
        'WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n'
        'OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER\n'
        'DEALINGS IN THE SOFTWARE.')


def bsd(year, holder):
    """Generates BSD licensing document.

    :param year: Copyright year.
    :type year: String
    :param holder: Copyright holder.
    :type holder: String
    :return: BSD license document.
    :rtype: String

    """
    return(
        f'Copyright {year}, {holder}\n\n'
        'Redistribution and use in source and binary forms, with or without\n'
        'modification, are permitted provided that the following conditions\n'
        'are met:\n\n'
        '1. Redistributions of source code must retain the above copyright\n'
        'notice, this list of conditions and the following disclaimer.\n'
        '2. Redistributions in binary form must reproduce the above\n'
        'copyright notice, this list of conditions and the following\n'
        'disclaimer in the documentation and / or other materials provided\n'
        'with the distribution.\n'
        '3. Neither the name of the copyright holder nor the names of its\n'
        'contributors may be used to endorse or promote products derived\n'
        'from this software without specific prior written permission.\n\n'
        'THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS\n'
        '\"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT\n'
        'LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS\n'
        'FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE\n'
        'COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,\n'
        'INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL\n'
        'DAMAGES(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE\n'
        'GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS\n'
        'INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,\n'
        'WHETHER IN CONTRACT, STRICT LIABILITY, OR\n'
        'TORT(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF\n'
        'THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF\n'
        'SUCH DAMAGE.')


def apache(year, holder):
    """Generates an ISC license document.

    :param year: Copyright year.
    :type year: String
    :param holder: Copyright holder.
    :type holder: String
    :return: Apache license document.
    :rtype: String

    """
    return(
        f'Copyright {year}, {holder}\n\n'
        'Licensed under the Apache License, Version 2.0 (the "License"); you\n'
        'may not use this file except in compliance with the License. You\n'
        'may obtain a copy of the License at\n\n'
        '    http://www.apache.org/licenses/LICENSE-2.0\n\n'
        'Unless required by applicable law or agreed to in writing, software\n'
        'distributed under the License is distributed on an \"AS IS\" BASIS,\n'
        'WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, neither express or\n'
        'implied. See the License for the specific language governing\n'
        'permissions and limitations under the License.')


def isc(year, holder):
    """Generates an ISC license document.

    :param year: Copyright year.
    :type year: String
    :param holder: Copyright holder.
    :type holder: String
    :return: ISC License document.
    :rtype: String

    """
    return(
        f'Copyright {year}, {holder}\n\n'
        'Permission to use, copy, modify, and/or distribute this software\n'
        'for any purpose with or without fee is hereby granted, provided\n'
        'that the above copyright notice and this permission notice\n'
        'appear in all copies.\n\n'
        'THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL\n'
        'WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED\n'
        'WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE\n'
        'AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR\n'
        'CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM\n'
        'LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,\n'
        'NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN\n'
        'CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.'
        )


def wtfpl(year, holder):
    """Creates a WTFPL license document.

    :param year: Copyright year.
    :type year: String
    :param holder: Copyright holder.
    :type holder: String
    :return: WTFPL license document.
    :rtype: String

    """
    return(
        f'Copyright(C) {year} {holder}\n\n'
        'WTFPL LICENSE\n'
        '``````````````````````````\n'
        'TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION\n\n'
        '    0. You just DO WHAT THE FUCK YOU WANT TO.'
        )
