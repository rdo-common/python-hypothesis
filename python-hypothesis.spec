%global srcname hypothesis
%global sum A library for property based testing

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{srcname}
Version:        1.11.2
Release:        3%{?dist}
Summary:        %{sum}

License:        MPLv2.0
URL:            https://github.com/DRMacIver/hypothesis
Source0:        https://github.com/DRMacIver/hypothesis/archive/v%{version}.tar.gz#/hypothesis-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-sphinx
# Test dependencies
BuildRequires:  numpy
BuildRequires:  pytest
BuildRequires:  pytz
#BuildRequires:  python-django
BuildRequires:  python-flake8

%description
Hypothesis is a library for testing your Python code against a much
larger range of examples than you would ever want to write by
hand. It’s based on the Haskell library, Quickcheck, and is designed
to integrate seamlessly into your existing Python unit testing work
flow.


%package     -n python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}
Obsoletes:      python-%{srcname} < 1.11.1-1
%if 0%{?with_python3}
# needed only by hypothesis-extras
Suggests:       numpy
# fake-factory not packaged yet
# Suggests:       python2-fake-factory
Suggests:       pytz
# Django support requires fake-factory
# TODO - update to python2-django once available
# Enhances:       python-django
%endif

%description -n python2-%{srcname}
Hypothesis is a library for testing your Python code against a much
larger range of examples than you would ever want to write by
hand. It’s based on the Haskell library, Quickcheck, and is designed
to integrate seamlessly into your existing Python unit testing work
flow.


%if 0%{?with_python3}
%package     -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}
# needed only by hypothesis-extras
# fake-factory not packaged yet
# Suggests:       python3-fake-factory
Suggests:       python3-numpy
Suggests:       python3-pytz
# Django support requires fake-factory
# Enhances:       python3-django

BuildRequires:  python3-devel
#BuildRequires:  python3-django
BuildRequires:  python3-flake8
BuildRequires:  python3-numpy
BuildRequires:  python3-pytest
BuildRequires:  python3-pytz



%description -n python3-%{srcname}
Hypothesis is a library for testing your Python code against a much
larger range of examples than you would ever want to write by
hand. It’s based on the Haskell library, Quickcheck, and is designed
to integrate seamlessly into your existing Python unit testing work
flow.
%endif


%prep
%autosetup -n %{srcname}-%{version}

# remove shebang, mergedbs gets installed in sitelib
%{__sed} -i -e 1,2d src/hypothesis/tools/mergedbs.py
# remove Django tests for now
rm -rf tests/django
# remove fakefactory tests, not packaged yet
rm -rf tests/fakefactory
# remove slow tests
rm -rf tests/nocover


%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif
(cd docs && READTHEDOCS=True make man)


%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif
%{__install} -Dp -m 644 docs/_build/man/hypothesis.1 \
             $RPM_BUILD_ROOT%{_mandir}/man1/hypothesis.1


%check
#{__python2} setup.py test

# remove py2-specific tests
rm -rf tests/py2
#{__python3} setup.py test


%files -n python2-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python2_sitelib}/*
%{_mandir}/man1/hypothesis.1*

%if 0%{?with_python3}
%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/*
%{_mandir}/man1/hypothesis.1*
%endif

%changelog
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Sep 25 2015 Michel Salim <salimma@fedoraproject.org> - 1.11.2-1
- Update to 1.11.2

* Sun Sep 20 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.11.1-1
- Update to 1.11.1

* Wed Sep  2 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.11.0-1
- Update to 1.11.0

* Tue Sep  1 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.10.6-3
- Re-disable tests for now

* Tue Sep  1 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.10.6-2
- Disable Python3 tests - need debugging on ARM builders

* Mon Aug 31 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.10.6-1
- Update to 1.10.6
- Enable tests

* Fri Aug  7 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.10.0-1
- Update to 1.10

* Wed Jul 29 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.9.0-1
- Update to 1.9.0

* Fri Jul 24 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.8.5-2
- Remove she-bang from tools/mergedbs.py
- Include manpage

* Fri Jul 24 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.8.5-1
- Update to 1.8.5
- Make Python3 build unconditional

* Thu Jul 23 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.8.2-1
- Initial package
