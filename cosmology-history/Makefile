# cosmology-history infographic — build pipeline
#
# Targets:
#   make           = compile cosmology-history.pdf (= default)
#   make view      = open the PDF in macOS Preview
#   make png       = export 300 DPI PNG (= for web sharing)
#   make clean     = remove aux files (keep PDF)
#   make distclean = remove all generated files including PDF

TEX := cosmology-history.tex
PDF := cosmology-history.pdf
PNG := cosmology-history.png

ENGINE := lualatex
LATEXOPTS := -interaction=nonstopmode -halt-on-error

.PHONY: all view png clean distclean

all: $(PDF)

$(PDF): $(TEX)
	$(ENGINE) $(LATEXOPTS) $(TEX)
	@# pgfplots sometimes needs a second pass for reference resolution
	$(ENGINE) $(LATEXOPTS) $(TEX)

view: $(PDF)
	open $(PDF)

# 300 DPI PNG export for web / chat sharing
png: $(PDF)
	@command -v pdftoppm >/dev/null 2>&1 || { echo "Install poppler: brew install poppler"; exit 1; }
	pdftoppm -r 300 -png $(PDF) cosmology-history
	@mv cosmology-history-1.png $(PNG) 2>/dev/null || true
	@echo "Wrote $(PNG)"

clean:
	rm -f *.aux *.log *.out *.synctex.gz *.fls *.fdb_latexmk *.toc

distclean: clean
	rm -f $(PDF) $(PNG)
