class TreeNode:
    def __init__(self, feature=None, value=None, left=None, right=None):
        self.feature = feature
        self.value = value
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None

def build_triage_tree():
    merah_node = TreeNode(value="MERAH")
    kuning_node = TreeNode(value="KUNING")
    hijau_node = TreeNode(value="HIJAU")
    hitam_node = TreeNode(value="HITAM")

    bisa_pcr = TreeNode(feature="Bisa PCR?", left=merah_node, right=kuning_node)
    urine_gelap = TreeNode(feature="Urine Gelap?", left=merah_node, right=merah_node)
    pergerakan_organ = TreeNode(feature="Pergerakan Organ?", left=merah_node, right=hitam_node)
    tidak_ada_nadi = TreeNode(feature="Tidak ada Nadi?", left=merah_node, right=hitam_node)
    sadar = TreeNode(feature="Sadar?", left=kuning_node, right=hijau_node)
    nadi_stabil = TreeNode(feature="Nadi Stabil?", left=kuning_node, right=hijau_node)
    riwayat_penyakit = TreeNode(feature="Riwayat Penyakit?", left=hijau_node, right=kuning_node)
    luka_berat = TreeNode(feature="Luka Berat?", left=hijau_node, right=kuning_node)

    obstruksi = TreeNode(feature="Obstruksi?", left=bisa_pcr, right=urine_gelap)
    nadi_lemah = TreeNode(feature="Nadi Lemah?", left=pergerakan_organ, right=tidak_ada_nadi)
    responsif = TreeNode(feature="Responsif?", left=sadar, right=nadi_stabil)
    ada_luka = TreeNode(feature="Ada Luka?", left=riwayat_penyakit, right=luka_berat)

    warna_kulit_abnormal = TreeNode(feature="Warna Kulit Abnormal?", left=obstruksi, right=nadi_lemah)
    nafas_normal = TreeNode(feature="Nafas Normal?", left=responsif, right=ada_luka)

    root_node = TreeNode(feature="Apakah pasien bisa bernafas?", left=warna_kulit_abnormal, right=nafas_normal)
    return root_node
