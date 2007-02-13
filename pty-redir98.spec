Summary:	Creates a pair of pseudo-terminals
Summary(pl.UTF-8):	Tworzy parę pseudo-terminali
Name:		pty-redir98
Version:	1.0
Release:	3
License:	GPL
Group:		Applications/Terminal
Source0:	ftp://ftp.pld.org.pl/software/pty-redir98/%{name}-%{version}.tar.gz
# Source0-md5:	91c6d9069cbc4717d60c9c5a219cbe49
URL:		ftp://ftp.pld.org.pl/software/pty-redir98/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pty-redir98 is a remake of old "pty-redir" application, using Unix98
PTYs. It creates a pair of pseudo-terminals for any application to
use. For example it allows running PPP over SSH by attaching SSH
input/output to a pseudo-tty master and running pppd on corresponding
slave.

%description -l pl.UTF-8
pty-redir98 jest przeróbką starego programu "pty-redir", używającą
pseudo-terminali zgodnie z semantyką Unix98. Tworzy parę
pseudo-terminali które dowolna aplikacja może wykorzystać. Na przykład
umożliwia uruchomienie PPP po SSH przez podczepienie wejścia/wyjścia
SSH do nadrzędnego pseudo-terminala i uruchomienie pppd na
odpowiadającym mu pseudo-terminalu podrzędnym.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
