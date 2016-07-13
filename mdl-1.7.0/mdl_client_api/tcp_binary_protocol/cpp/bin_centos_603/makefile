all: mdl_api_demo

SRCDIR := ../api_demo
OUTDIR := ./
LIBDIR := -L../../../../mdl_proxy/centos_603/
SODIR := -Wl,-rpath=./ 
CPPFLAGS := -O3 -c -fmessage-length=0
INCS := -I../
LIBS := -lmdl_api -ldl -lpthread -lrt
OBJS = \
	./mdl_api_demo.o

%.o: $(SRCDIR)/%.cpp
	@echo 'Compiling : $<'
	g++ $(MACRODEF) $(INCS) $(CPPFLAGS) -o "$@" "$<"
mdl_api_demo: $(OBJS)
	@echo 'Linking :'
	[ -h ./libmdl_api.so ] || ln -sf ../../../../mdl_proxy/centos_603/libmdl_api.so ./libmdl_api.so
	[ -h ./libicuuc.so.48 ] || ln -sf ../../../../mdl_proxy/centos_603/libicuuc.so.48 ./libicuuc.so.48
	[ -h ./libicudata.so.48 ] || ln -sf ../../../../mdl_proxy/centos_603/libicudata.so.48 ./libicudata.so.48
	g++ $(LIBDIR) $(SODIR) -o "$(OUTDIR)$@" $(OBJS) $(LIBS)


.PHONY: clean
clean:
	rm -f ./mdl_api_demo.o  ./mdl_api_demo

