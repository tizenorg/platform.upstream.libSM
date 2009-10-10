#
# Copyright 2009 Sun Microsystems, Inc.  All rights reserved.
#
# Permission to use, copy, modify, distribute, and sell this software and its
# documentation for any purpose is hereby granted without fee, provided that
# the above copyright notice appear in all copies and that both that
# copyright notice and this permission notice appear in supporting
# documentation.
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE OPEN GROUP BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# Except as contained in this notice, the name of the copyright holders shall
# not be used in advertising or otherwise to promote the sale, use or
# other dealings in this Software without prior written authorization
# from the copyright holders.
#

# Based on xc/doc/specs/SM/Makefile from X11R6.9

doc_sources = macros.t SMlib.ms

doc_input = $(doc_sources:%=$(srcdir)/%)

EXTRA_DIST = $(doc_sources)

if BUILD_DOCS
doc_DATA = SMlib.txt SMlib.ps SMlib.html

CLEANFILES = $(doc_DATA)
MOSTLYCLEANFILES = index.*

# Pass version string as a troff string for substitution
GROFF_DEFS = -dxV="$(PACKAGE_STRING)"

# -t to run through tbl
GROFF_FLAGS = -t -ms $(GROFF_DEFS)

SMlib.ps: $(doc_input)
	-$(AM_V_GEN) $(GROFF) -Tps $(GROFF_FLAGS) $(doc_input) \
	 2> index.raw > $@
	@if grep '^[^1-9.]' index.raw | grep -v warning; then exit 1; \
	 else test $$? -le 1; fi

SMlib.txt: $(doc_input)
	$(AM_V_GEN) env GROFF_NO_SGR=TRUE $(GROFF) -Tascii $(GROFF_FLAGS) \
	 $(doc_input) 2> index.txt.raw | col -b > $@

SMlib.html: $(doc_input)
	$(AM_V_GEN) $(GROFF) -Thtml $(GROFF_FLAGS) $(doc_input) \
	 2> index.html.raw > $@

endif BUILD_DOCS
