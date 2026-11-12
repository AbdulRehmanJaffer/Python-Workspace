import gradio as gr
import pandas as pd
import did_you_mean as dym


def table_frame(a, b):
    """Turn the edit-distance table into a labelled grid."""
    table = dym.build_table(a, b)
    headers, seen = ["", "."], {}
    for ch in b:
        seen[ch] = seen.get(ch, 0) + 1            # so add extra spaces
        headers.append(ch + " " * (seen[ch] - 1))
    rows = []
    for i, row in enumerate(table):
        label = "." if i == 0 else a[i - 1]
        rows.append([label] + [f"{v:g}" for v in row])
    return pd.DataFrame(rows, columns=headers)


def search(query, keyboard, swaps):
    # Gradio calls this function whenever the text or a checkbox changes.
    # It returns one value for each output below, in the same order.
    dym.USE_KEYBOARD, dym.USE_SWAPS = keyboard, swaps
    query = query.lower().strip()
    if not query:
        return "Type a dish name above.", None, None
    dish, message = dym.did_you_mean(query)
    top = pd.DataFrame(dym.suggest(query, k=5), columns=["dish", "edit distance", "orders"])
    target = dish or top.iloc[0]["dish"]
    return (f"## {message}\n_Allowed typos for a {len(query)}-letter search: "
            f"{dym.max_typos(query)}_", top, table_frame(query, target))


with gr.Blocks(title="Did You Mean?") as demo:
    gr.Markdown("# Food search with \"Did you mean?\"")
    query = gr.Textbox(label="Search the menu", value="biriyani")
    with gr.Row():
        keyboard = gr.Checkbox(value=True, label="Upgrade 1: neighbouring keys cost 0.5")
        swaps = gr.Checkbox(value=True, label="Upgrade 2: swapped letters cost 1")
    answer = gr.Markdown()
    with gr.Row():
        top = gr.Dataframe(label="Closest dishes")
        grid = gr.Dataframe(label="Edit-distance table (bottom-right cell = the answer)")
    gr.Examples([["piza"], ["cske"], ["noodels"], ["panner tika"], ["lasi"]], inputs=query)

    inputs = [query, keyboard, swaps]
    outputs = [answer, top, grid]
    for trigger in (query.change, keyboard.change, swaps.change):
        trigger(search, inputs, outputs)
    demo.load(search, inputs, outputs)

if __name__ == "__main__":
    demo.launch()