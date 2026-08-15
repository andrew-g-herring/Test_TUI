Name:           python-test-tui
Version:        1.0.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A centered red text terminal user interface built with blessed

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            ...
Source:         /home/andrew/Projects/Terminal/Test_TUI/dist/test_tui-1.0.0.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'test-tui' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-test-tui
Summary:        %{summary}

%description -n python3-test-tui %_description


%prep
%autosetup -p1 -n test_tui-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Automatically extracted from wheel
%pyproject_save_files __init__ main


%check
%pyproject_check_import


%files -n python3-test-tui -f %{pyproject_files}
%{_bindir}/Test_TUI-cmd


%changelog
%autochangelog
