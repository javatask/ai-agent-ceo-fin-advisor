import pandas as pd
import numpy as np
import random


def generate_bakery_network_data(start_date='2024-01-01', months=12, seed=42):
    """Generate synthetic financial data for a bakery network."""
    np.random.seed(seed)
    random.seed(seed)
    
    industries = ['schools', 'cafes', 'shops', 'factories', 'restaurants', 'hotels']
    dates = pd.date_range(start=start_date, periods=months, freq='M')
    
    data = []
    for date in dates:
        for industry in industries:
            # Base values varying by industry
            base_bookings = {
                'schools': 15000, 'cafes': 25000, 'shops': 20000,
                'factories': 35000, 'restaurants': 30000, 'hotels': 40000
            }
            
            # Add seasonal variations
            seasonal_factor = 1 + 0.2 * np.sin(2 * np.pi * date.month / 12)
            
            # Random variations
            random_factor = np.random.normal(1, 0.1)
            
            bookings = base_bookings[industry] * seasonal_factor * random_factor
            # Billings are typically 85-95% of bookings
            billing_rate = np.random.uniform(0.85, 0.95)
            billings = bookings * billing_rate
            
            data.append({
                'date': date,
                'industry': industry,
                'bookings': round(bookings, 2),
                'billings': round(billings, 2),
                'billing_rate': round(billing_rate * 100, 2)
            })
    
    return pd.DataFrame(data)

def analyze_industry_performance(df, industry=None, date_range=None):
    """
    Analyze financial performance by industry.
    
    Args:
        df: DataFrame with bakery network data
        industry: Specific industry to analyze (optional)
        date_range: Tuple of (start_date, end_date) for analysis period
    """
    if date_range:
        df = df[(df['date'] >= date_range[0]) & (df['date'] <= date_range[1])]
    
    if industry:
        df = df[df['industry'] == industry]
    
    analysis = {
        'total_bookings': df['bookings'].sum(),
        'total_billings': df['billings'].sum(),
        'avg_billing_rate': df['billing_rate'].mean(),
        'industry_summary': df.groupby('industry').agg({
            'bookings': 'sum',
            'billings': 'sum',
            'billing_rate': 'mean'
        }).round(2),
        'monthly_trends': df.groupby('date').agg({
            'bookings': 'sum',
            'billings': 'sum'
        }).round(2)
    }
    
    return analysis

def format_analysis_to_string(analysis):
    """Convert analysis results to formatted string."""
    output = []
    
    output.append("=== BAKERY NETWORK ANALYSIS ===")
    output.append(f"\nOverall Performance:")
    output.append(f"Total Bookings: ${analysis['total_bookings']:,.2f}")
    output.append(f"Total Billings: ${analysis['total_billings']:,.2f}")
    output.append(f"Average Billing Rate: {analysis['avg_billing_rate']:.1f}%")
    
    # Industry Summary
    output.append("\nIndustry Summary:")
    industry_df = analysis['industry_summary'].copy()
    industry_df['bookings'] = industry_df['bookings'].apply(lambda x: f"${x:,.2f}")
    industry_df['billings'] = industry_df['billings'].apply(lambda x: f"${x:,.2f}")
    industry_df['billing_rate'] = industry_df['billing_rate'].apply(lambda x: f"{x:.1f}%")
    output.append(industry_df.to_string())
    
    # Monthly Trends
    output.append("\nMonthly Trends:")
    trends_df = analysis['monthly_trends'].copy()
    trends_df['bookings'] = trends_df['bookings'].apply(lambda x: f"${x:,.2f}")
    trends_df['billings'] = trends_df['billings'].apply(lambda x: f"${x:,.2f}")
    output.append(trends_df.to_string())
    
    return '\n'.join(output)

# Example usage
if __name__ == "__main__":
    # Generate sample data
    df = generate_bakery_network_data()
    
    # Example analysis for all industries
    analysis = analyze_industry_performance(df)
    print(f"Total Network Bookings: ${analysis['total_bookings']:,.2f}")
    print(f"Average Billing Rate: {analysis['avg_billing_rate']:.1f}%")
    
    # Example analysis for specific industry
    cafe_analysis = analyze_industry_performance(
        df, 
        industry='cafes',
        date_range=('2024-01-01', '2024-06-30')
    )
    print("\nCafe Performance (First Half):")
    print(f"Total Bookings: ${cafe_analysis['total_bookings']:,.2f}")