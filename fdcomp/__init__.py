import uproot
import re

def pretty_key(key, replacer=re.compile(";.*")):
    return re.sub(replacer, "", key.decode("utf-8"))

class fdfile():
    """Class that represents a fitdiagnostics file"""
    def __init__(self, path, fits=['fit_s', 'fit_b', 'prefit']):
        self._path = path
        self._fits = fits
        self._histograms = {}
        self.load()

    def load(self):
        """Method that loads all histograms from disk to memory"""
        f = uproot.open(self._path)
        for fit_name in self._fits:
            for cat_name, category_dir in f[f"shapes_{fit_name}"].items():
                for proc_name, histo in category_dir.items():
                    key = (fit_name, pretty_key(cat_name), pretty_key(proc_name))
                    self._histograms[key] = histo

    def get_histograms(self, fit_name, cat_name):
        """Getter method for a dictionary of histograms for given fit + category"""
        return {k[2] : v for k,v in self._histograms.items() if k[0]==fit_name and v[1]==cat_name}

    def get_histogram(self, fit_name, cat_name, proc_name):
        """Getter method for a single histogram"""
        key = (fit_name, cat_name, proc_name)
        return self._histograms[key]

    def apply_name_map(self, cat_map={}, proc_map={}):
        """Renaming method to change category and/or process naming convention"""
        tmp = {}
        for key, histo in self._histograms.items():
            fit_name, cat_name, proc_name = key
            new_cat_name = cat_map.get(cat_name, cat_name)
            new_proc_name = proc_map.get(proc_name, proc_name)
            new_key = (fit_name, new_cat_name, new_proc_name)
            tmp[new_key] = histo
        self._histograms = tmp
    def get_processes(self):
        return set([k[2] for k in self._histograms.keys()])
    def get_categories(self):
        return set([k[1] for k in self._histograms.keys()])