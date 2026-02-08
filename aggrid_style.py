import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode


def show_streamlit_style_grid(df, height=600):

    gb = GridOptionsBuilder.from_dataframe(df)

    # 🔹 DEFAULT COLUMN SETTINGS (CRITICAL)
    gb.configure_default_column(
        editable=True,            # ✅ ENABLE EDITING
        wrapText=True,
        autoHeight=True,
        sortable=True,
        filter=True,
        resizable=True,
        headerClass="wrap-header"
    )

    # 🔹 Fix S.No column (read-only)
    for col in df.columns:
        if col.lower() in ["s.no", "sno", "sr.no", "sl.no"]:
            gb.configure_column(
                col,
                editable=False,
                width=70,
                cellStyle={"textAlign": "center", "fontWeight": "600"}
            )

    gb.configure_grid_options(
        headerHeight=80,
        rowHeight=36,
        stopEditingWhenCellsLoseFocus=True  # ✅ important
    )

    grid_response = AgGrid(
        df,
        gridOptions=gb.build(),
        update_mode=GridUpdateMode.VALUE_CHANGED,  # ✅ CRITICAL
        enable_enterprise_modules=True,             # ✅ REQUIRED
        fit_columns_on_grid_load=True,
        use_container_width=True,
        height=height,
        theme="streamlit",
        allow_unsafe_jscode=True
    )

    return grid_response["data"]
