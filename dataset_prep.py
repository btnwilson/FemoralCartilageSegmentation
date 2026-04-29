def prepare_dataset():
    """
    Build a slice-level metadata table for cartilage MRI segmentation.

    Scans patient folders for left and right knee MRI/mask .mat files, records
    slice indices, and flags whether each slice contains any, femoral, or tibial
    cartilage annotations.
    """
    data = []
    series_info = {
        "Left": "401",
        "Right": "1401",
    }

    patient_dirs = sorted(
        d for d in os.listdir(".")
        if os.path.isdir(d) and d.isdigit()
    )

    for patient_id in tqdm(patient_dirs, desc="Processing patients"):
        for side, series_id in series_info.items():
            mri_file = os.path.join(patient_id, f"T1rho_S{series_id}.mat")
            mask_file = os.path.join(patient_id, f"T1rho_S{series_id}_prois.mat")

            if not (os.path.exists(mri_file) and os.path.exists(mask_file)):
                continue

            try:
                mri_data = loadmat(mri_file)
                mask_data = loadmat(mask_file)

                num_slices = mri_data["v"].shape[2]
                rsl = mask_data["rsl"].flatten() - 1
                rslf = mask_data.get("rslf", np.array([])).flatten() - 1
                rslt = mask_data.get("rslt", np.array([])).flatten() - 1

                for slice_idx in range(num_slices):
                    data.append({
                        "patient_id": patient_id,
                        "side": side,
                        "mri_file": mri_file,
                        "mask_file": mask_file,
                        "slice_idx": slice_idx,
                        "has_mask": slice_idx in rsl,
                        "has_femoral": slice_idx in rslf,
                        "has_tibial": slice_idx in rslt,
                    })

            except KeyError as e:
                print(f"Missing expected key in {patient_id} {side} files: {e}")
            except Exception as e:
                print(f"Error processing {patient_id} {side} files: {e}")

    df = pd.DataFrame(data)
    df.to_csv("cartilage_dataset.csv", index=False)

    print(f"Dataset prepared with {len(df)} slices")
    print(f"Slices with femoral cartilage: {df['has_femoral'].sum()}")
    print(f"Slices with tibial cartilage: {df['has_tibial'].sum()}")

    return df
