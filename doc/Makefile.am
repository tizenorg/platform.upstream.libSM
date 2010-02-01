#
# Copyright 2009 Sun Microsystems, Inc.  All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice (including the next
# paragraph) shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
#

# Based on xc/doc/specs/SM/Makefile from X11R6.9

doc_sources = macros.t SMlib.ms xsmp.ms

EXTRA_DIST = $(doc_sources)

if ENABLE_DOCS
if HAVE_GROFF
doc_DATA = SMlib.txt SMlib.ps SMlib.html xsmp.txt xsmp.ps xsmp.html
imagesdir = $(docdir)/images

CLEANFILES = $(doc_DATA)
MOSTLYCLEANFILES = index.*

install-data-local:
	test -z "$(imagesdir)" || $(MKDIR_P) "$(DESTDIR)$(imagesdir)"
	@d="$(srcdir)/images/"; \
	list=`ls $$d`; \
	for p in $$list; do \
	  echo " $(docDATA_INSTALL) '$$d$$p' '$(DESTDIR)$(imagesdir)/$$p'"; \
	  $(docDATA_INSTALL) "$$d$$p" "$(DESTDIR)$(imagesdir)/$$p"; \
	done;

uninstall-local:
	@if test -n $(DESTDIR)$(imagesdir); then \
	  if test -d $(DESTDIR)$(imagesdir); then \
	    list=`ls $(DESTDIR)$(imagesdir)`; \
	    for p in $$list; do \
	      echo " rm -f '$(DESTDIR)$(imagesdir)/$$p'"; \
	      rm -f "$(DESTDIR)$(imagesdir)/$$p"; \
	    done \
	  fi; \
	fi;

mostlyclean-local:
	@rm -fr images

# Pass version string as a troff string for substitution
GROFF_DEFS = -dxV="$(PACKAGE_STRING)"

# -t to run through tbl
GROFF_FLAGS = -t -ms $(GROFF_DEFS) $(srcdir)/macros.t

SUFFIXES = .ms .ps .txt .html

.ms.ps:
	-$(AM_V_GEN) $(GROFF) -Tps $(GROFF_FLAGS) $< 2> index.$@.raw > $@
	@if grep '^[^1-9.]' index.$@.raw | grep -v warning; then exit 1; \
	 else test $$? -le 1; fi

.ms.txt:
	$(AM_V_GEN) env GROFF_NO_SGR=TRUE $(GROFF) -Tutf8 $(GROFF_FLAGS) \
	 $< 2> index.$@.raw > $@

.ms.html:
	$(AM_V_GEN) $(GROFF) -Thtml -P-Dimages -P-I$*-image $(GROFF_FLAGS) $< 2> index.$@.raw > $@

endif HAVE_GROFF
endif ENABLE_DOCS
