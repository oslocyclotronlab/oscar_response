import matplotlib.pyplot as plt
import numpy as np
import ompy as om
import logging

###########


def plot_compare(response, R, Rmama, raw_base_folder):
    """
    Plots and compares the first N interpolations to raw/simulated spectra
    """
    fig, axmat = plt.subplots(3, 3)
    fig_diff, axmat_diff = plt.subplots(3, 3)

    fig.suptitle("compare response functions")
    fig_diff.suptitle("(interp.-raw)/raw in %")

    Eresp = response.resp['Eg']

    for i, E in enumerate(Eresp):
        if i == len(axmat.flatten()):
            break
        ax = axmat.flatten()[i]
        axdiff = axmat_diff.flatten()[i]
        E_ = R.Ex[R.index_Ex(E)]
        values, Eg = R.projection(axis="Eg", Emin=E_, Emax=E_)
        ompy = om.Vector(values, Eg)

        E_ = Rmama.Ex[Rmama.index_Ex(E)]
        values, Eg = Rmama.projection(axis="Eg", Emin=E_, Emax=E_)
        mama = om.Vector(values, Eg)

        ompy.plot(ax=ax, linestyle="--", label=f"ompy {E_:.0f}")
        mama.plot(ax=ax, linestyle=":", label=f"mama {E_:.0f}")

        try:
            raw = om.Vector(path=raw_base_folder + f"/raw{E:.0f}")
            raw.values = om.rebin_1D(raw.values, raw.E, response.Eout)
            raw.values /= raw.values.sum()
            raw.E = response.Eout
            raw.plot(ax=ax, label="raw", linestyle="-", alpha=0.5)

            ompy_diff = ((ompy - raw) / raw) * 100
            mama_diff = ((mama - raw) / raw) * 100

            ompy_diff.plot(ax=axdiff, linestyle="--", label=f"ompy {E_:.0f}")
            mama_diff.plot(ax=axdiff, linestyle=":", label=f"mama {E_:.0f}")
        except:
            print("didn't find raw")
            pass

        ax.legend()
        ax.set_yscale("log")
        ax.set_xlim(0, E + 2 * response.f_fwhm_abs(E))
        ax.set_ylim(1e-3, None)

        axdiff.axhline(0, color="r", alpha=0.3)
        axdiff.legend()
        axdiff.set_xlim(0, E + 2 * response.f_fwhm_abs(E))
        axdiff.set_ylim(-30, 30)

    return fig, fig_diff, axmat, axmat_diff


def plot_low_energy():
    fig, axmat = plt.subplots(3, 3)
    fig.suptitle("Interpolation in the low energies")

    Eresp = np.linspace(0, 800, 9)
    for i, E in enumerate(Eresp):
        if i == len(axmat.flatten()):
            break
        ax = axmat.flatten()[i]
        E_ = R.Ex[R.index_Ex(E)]
        values, Eg = R.projection(axis="Eg", Emin=E_, Emax=E_)
        ompy = om.Vector(values, Eg)

        ompy.plot(ax=ax, linestyle="--", label=f"ompy {E_:.0f}")
        ax.legend()
        ax.set_yscale("log")
        ax.set_xlim(0, E + 2 * response.f_fwhm_abs(E))
        ax.set_ylim(1e-3, None)


if __name__ == "__main__":
    # Import raw matrix into instance of om.Matrix() and plot it
    raw = om.example_raw('Si28')

    #########

    folderpath = "../oscar_response/nai2012_for_opt13"
    filepath = "../oscar_response/nai2012.zip"
    # folderpath = "../oscar_response/oscar2017_scale1.15"

    # Energy calibration of resulting response matrix:
    Eg = raw.Eg

    # Experimental relative FWHM at 1.33 MeV of resulting array
    fwhm_abs = 6.8 / 100 * 1330

    # load response
    # logger = om.introspection.get_logger('response_class', 'DEBUG')
    response = om.Response(folderpath)
    response.smooth_compton = False
    R, tab = response.interpolate(Eg, fwhm_abs, return_table=True)


    plot_low_energy()

    # plots1
    Rmama = om.Matrix(path="../example_data/resp.m")

    fig, axmat = plt.subplots(1, 2, constrained_layout=True)
    R.plot(scale="log", ax=axmat[0], vmin=5e-5, vmax=5e-1,
           midbin_ticks=False, title="ompy")
    lines, ax, _ = Rmama.plot(scale="log", ax=axmat[1],
                              vmin=5e-5, vmax=5e-1,
                              midbin_ticks=False, title="mama")
    fig.colorbar(lines, ax=ax, extend='both')

    # comparison plots
    plot_compare(response, R, Rmama, folderpath)
    plt.show()
