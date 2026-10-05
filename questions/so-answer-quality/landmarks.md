# Frontier — landmarks used so far (so-answer-quality)

Rows marked VALID bind the frontier; the rest record what was tried and how it failed.

| # | landmark | chain | verdict |
|---|---|---|---|
| 1 | The question's contribution is the same for both answers, so only the difference between the answers matters (comparison within the pair). | attempt 007 | ILL-FORMED |
| 2 | Rescale each component feature by how much it varies so that all groups count on equal terms. | attempt 007 | ILL-FORMED |
| 3 | One direction, fitted on train pair differences with a penalty and both orderings, ranks answers by how far they sit along it. | attempt 007 | ILL-FORMED |
| 4 | Field-evolution magnitudes alone, meaning how much an answer's latent fields are reworked across stages, carry a quality signal. | route 003 | VALID |
| 5 | Each component votes on its own, with a direction and a confidence weight taken from its train win-rate against a coin flip. | route 003 | VALID |
| 6 | Percentile ranks among pooled train answers put the components on a common scale without any spread-based rescaling or fitted direction. | route 003 | VALID |
| 7 | Visible effort, meaning log-scaled length plus runnable code blocks, is what voters see and reward. | attempt 008 | DUPLICATE |
| 8 | Reusing the question's distinctive (rarer, non-filler) terms is a sign the answer is relevant. | attempt 008 | DUPLICATE |
| 9 | A fixed, hand-set sum of surface cues, with no training and no model components, ranks the pair. | attempt 008 | DUPLICATE |
| 10 | Completeness counted as breadth: how many distinct kinds of content an answer covers (prose, code, links, lists, caveats, reasons, examples), each counted once and capped, not how much of any one kind. | route 004 | VALID |
| 11 | The coverage count uses no training and no model components, and it measures something different from length or from per-component votes. | route 004 | VALID |
| 12 | Vocabulary size works only as a bounded tie-break, and it can never outweigh one extra kind of content. | route 004 | VALID |
