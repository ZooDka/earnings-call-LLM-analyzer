"""
test_llm.py - Test the LLM analysis using a real IBM transcript without hitting the API.
Uses the actual IBM 2024Q1 transcript fetched earlier.
"""

import json
from llm_api import analyze_transcript

# Real IBM 2024Q1 transcript from Alpha Vantage
IBM_2024Q1 = """Olympia McNerney: Thank you. I'd like to welcome you to IBM's First Quarter 2024 Earnings Presentation. I'm Olympia McNerney, and I'm here today with Arvind Krishna, IBM's Chairman and Chief Executive Officer; and Jim Kavanaugh, IBM's Senior Vice President and Chief Financial Officer.

Arvind Krishna: Thank you for joining us. In the first quarter, we had solid performance across revenue and cash flow. These results are further proof of the quality of our portfolio and our hybrid cloud and AI strategy. We had good performance in Software, at the high end of our model; continued strength in Infrastructure, above our model; while Consulting was below model. Our cash flow generation is the strongest first quarter level we have reported in many years. Before we get into more detail on the quarter, let me address the announcement of our agreement to acquire HashiCorp for $6.4 billion. HashiCorp has a proven track record of helping clients manage the complexity of today's infrastructure by automating, orchestrating, and securing hybrid and multi-cloud environments. Inception to date, our book of business related to watsonx and generative AI is greater than $1 billion with sequential quarter-over-quarter growth.

James Kavanaugh: In the first quarter, we delivered $14.5 billion in revenue; $3 billion of adjusted EBITDA; $1.7 billion of operating pretax income; $1.68 operating earnings per share; and we generated free cash flow of $1.9 billion, up approximately $600 million year-over-year. Our revenue for the quarter was up 3% at constant currency. Software grew by 6%. Consulting was up 2%. Infrastructure had strong performance, delivering growth across all of our hardware offerings. We expanded operating gross margin by 100 basis points and operating pretax margin by 130 basis points over last year. We generated $1.9 billion of free cash flow, up $600 million year-over-year. Over the last 12 months, we generated free cash flow of $11.8 billion.

Arvind Krishna: Our Consulting revenue was up 2%. Solid demand for our offerings led to signings growth of 4%, our highest absolute first quarter signings in recent history. Our overall backlog remains healthy, up 7% year-over-year. We are seeing some pressure on smaller, more discretionary projects.

Arvind Krishna: Looking to the full year 2024, we are holding our view on our 2 primary metrics: revenue and free cash flow. We see full-year constant currency revenue growth in line with our mid-single-digit model. For free cash flow, we expect to generate about $12 billion. In Software, we continue to expect growth slightly above the high end of our mid-single-digit model. In Consulting, we now see mid-single-digit revenue growth with acceleration throughout the year. In Infrastructure, given product cycle dynamics, we expect revenue to decline."""

# Reuse 2022Q4 as the "prior quarter" mock (shorter placeholder)
IBM_2022Q4 = """Arvind Krishna: In the fourth quarter, we delivered solid revenue growth across our hybrid cloud and AI portfolio. Software grew 3%, Consulting grew 5%, and Infrastructure declined as expected due to product cycle timing. We generated strong free cash flow and returned capital to shareholders. Looking ahead to 2023, we expect mid-single-digit constant currency revenue growth and approximately $10.5 billion in free cash flow.

James Kavanaugh: Fourth quarter revenue was $16.7 billion, up 6% at constant currency. We delivered operating EPS of $3.60. Full year free cash flow came in at $9.3 billion. Consulting backlog grew double digits year-over-year. Red Hat revenue grew 9% for the quarter."""


if __name__ == "__main__":
    print("Running LLM analysis on IBM 2024Q1 vs 2022Q4 (mock data)...\n")

    result = analyze_transcript(
        transcript_current=IBM_2024Q1,
        transcript_prior=IBM_2022Q4,
        ticker="IBM",
        quarter_current="2024Q1",
        quarter_prior="2022Q4",
    )

    print(json.dumps(result, indent=2))
    print("\n✅ Success! LLM analysis pipeline is working correctly.")
